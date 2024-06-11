from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.translation import gettext as _

class ProductType(models.Model):
    title = models.CharField(_("Название"), max_length=50, unique=True, null=False)

    class Meta:
        verbose_name = _("Тип продукта")
        verbose_name_plural = _("Типы продуктов")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Product(models.Model):
    title = models.CharField(_("Название"), max_length=50, unique=True, null=False)
    type = models.ForeignKey("ProductType", verbose_name=_("Тип продукта"), on_delete=models.CASCADE, null=False)
    price = models.DecimalField(_("Цена"), max_digits=7, decimal_places=2, null=False)

    def get_upload_path(instance, filename):
        return f"product_img/{instance.title}/{filename}"
    
    img = models.ImageField(_("Картинка"), upload_to=get_upload_path, null=False, default="product_img/defautl.png")

    class Meta:
        verbose_name = _("Продукт")
        verbose_name_plural = _("Продукты")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
    
class Feedback(models.Model):
    author_full_name = models.CharField(_("Полное имя автора"), max_length=70, null=False)
    author_tg = models.CharField(_("Телеграмм автора"), max_length=30, null=False)
    product = models.ForeignKey("Product", verbose_name=_("Продукт"), on_delete=models.CASCADE, null=False)
    content = models.CharField(_("Содержание"), max_length=200)
    estimation = models.IntegerField(_("Оценка"), validators=[MinValueValidator(1), MaxValueValidator(5)])
    date = models.DateTimeField(_("Время создания"), auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = _("Отзыв")
        verbose_name_plural = _("Отзывы")

        constraints = [
            models.CheckConstraint(
                check=models.Q(estimation__gte=1) & models.Q(estimation__lte=5),
                name='estimation_range'
            ),
        ]

    def __str__(self):
        return self.author_full_name

    def get_absolute_url(self):
        return reverse("feedback_detail", kwargs={"pk": self.pk})
