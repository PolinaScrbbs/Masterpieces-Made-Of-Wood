import re
from django.http import HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Avg
from django.urls import reverse
from django.views import View
from .models import ProductType, Product, Feedback
def index(request):

    context = {
        "title": "Шедевры из дерева",
    }

    return render(request, 'index.html', context)

def about(request):

    context = {
        "title": "О нас",
    }

    return render(request, 'about_us.html', context)

def delivery(request):

    context = {
        "title": "Доставка",
    }

    return render(request, 'delivery.html', context)

class FeedbackView(View):
    def post(self, request):
        author_full_name = request.POST.get('author_full_name')
        author_tg = request.POST.get('author_tg')
        product_id = int(request.POST.get('product'))
        content = request.POST.get('content')
        estimation = int(request.POST.get('estimation'))

        error = None

        if Feedback.objects.filter(author_tg=author_tg, product_id=product_id).exists():
            error = "Вы уже оставляли отзыв об этом продукте."
        
        if error is None:
            error = self.validate_feedback(author_full_name, author_tg, product_id, content, estimation)

        if error is not None:
            context = self.get_context()
            context["error"] = error
            return render(request, 'reviews.html', context)
        
        product = get_object_or_404(Product, id=product_id)

        feedback = Feedback(
            author_full_name=author_full_name.title(),
            author_tg=author_tg,
            product=product,
            content=content,
            estimation=estimation
        )
        feedback.save()

        return render(request, 'reviews.html', self.get_context())

    def get(self, request):
        return render(request, 'reviews.html', self.get_context())
    
    def get_context(self):
        products = Product.objects.all()
        feedbacks = Feedback.objects.all()
        reviews_count = feedbacks.count()

        average_estimation = self.get_average_estimation()

        context = {
            'products': products,
            'reviews': feedbacks,
            'reviews_count': reviews_count,
            'average_estimation': average_estimation,
        }

        return context

    def get_average_estimation(self):
        feedbacks = Feedback.objects.all()
        if feedbacks.exists():
            avg_estimation = feedbacks.aggregate(Avg('estimation'))['estimation__avg']
            if avg_estimation is not None:
                return round(avg_estimation, 1)
        return 0
    
    def validate_feedback(self, author_full_name, author_tg, product_id, content, estimation):
        validators = [
            (lambda: not re.match(r'^[А-ЯЁёа-яё]+\s[А-ЯЁёа-яё]+\s[А-ЯЁёа-яё]+$', author_full_name), "Недопустимый формат для ФИО"),
            (lambda: len(author_full_name) > 70, "Длина ФИО превышает 70 символов"),
            (lambda: len(author_full_name) < 15, "Длина ФИО меньше 15 символов"),
            (lambda: not re.match(r'^@[a-zA-Z0-9_]+$', author_tg), "Недопустимый формат для Телеграм тега"),
            (lambda: len(author_tg) > 30, "Длина Телеграм тега превышает 30 символов"),
            (lambda: len(author_tg) < 3, "Длина Телеграм тега меньше 3 символов"),
            (lambda: not re.match(r'^[А-Яа-я0-9\s,.!?:;"\'()]+$', content), "Недопустимый формат для содержания отзыва"),
            (lambda: len(content) > 200, "Длина содержания отзыва превышает 200 символов"),
            (lambda: not (isinstance(int(product_id), int) and isinstance(int(estimation), int)), "Недопустимый тип данных для идентификатора продукта или оценки"),
            (lambda: not (product_id and estimation), "Требуется идентификатор продукта и его оценка"),
            (lambda: not self.check_previous_reviews(author_tg, author_full_name), "Имя автора в текущем отзыве должно совпадать с его предыдущими отзывами")
        ]

        for condition, error_message in validators:
            if condition():
                return error_message
        
        return None
    
    def check_previous_reviews(self, author_tg, author_full_name):
        previous_reviews = Feedback.objects.filter(author_tg=author_tg)
        if previous_reviews != []:
            for review in previous_reviews:
                if review.author_full_name != author_full_name:
                    print(f"{review.author_full_name} != {author_full_name}")
                    return False
        return True

def services(request, *args, **kwargs):
    type_title = kwargs.get("type").replace("_", " ")
    type = ProductType.objects.get(title=type_title)

    context = {
        "title": type_title,
        "description": type.description,
        # "img_url": type.img.url,
        "products": Product.objects.filter(type = type).order_by("price")
    }

    return render(request, 'services.html', context)

def product(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        print(product_id)
        try:
            product = Product.objects.get(id=product_id)
            return JsonResponse({
                'id': product.id,
                'title': product.title,
                'description': product.description if product.description else "Описание",
                'price': product.price,
                'img_url': product.img.url
            })
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


