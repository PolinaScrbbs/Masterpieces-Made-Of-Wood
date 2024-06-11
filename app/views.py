from django.shortcuts import render
from django.db.models import Avg
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

def get_average_estimation():
    return Feedback.objects.aggregate(average_estimation=Avg('estimation'))['average_estimation']

def reviews(request):

    context = {
        "title": "Отзывы",
        "reviews": Feedback.objects.all(),
        "reviews_count": Feedback.objects.all().count(),
        "average_estimation": get_average_estimation()
    }

    return render(request, 'reviews.html', context)

def services(request, *args, **kwargs):
    type_title = kwargs.get("type").replace("_", " ")

    context = {
        "title": type_title,
        "products": Product.objects.filter(type = ProductType.objects.get(title=type_title)).order_by("price")
    }

    print(Product.objects.filter(type = ProductType.objects.get(title=type_title)))

    return render(request, 'services.html', context)
