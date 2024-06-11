# Generated by Django 5.0.6 on 2024-06-11 09:20

import app.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('img', models.ImageField(default='product_img/defautl.png', upload_to=app.models.Product.get_upload_path, verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип продукта',
                'verbose_name_plural': 'Типы продуктов',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_full_name', models.CharField(max_length=70, verbose_name='Полное имя автора')),
                ('author_tg', models.CharField(max_length=30, verbose_name='Телеграмм автора')),
                ('content', models.CharField(max_length=200, verbose_name='Содержание')),
                ('estimation', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Время создания')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producttype', verbose_name='Тип продукта'),
        ),
        migrations.AddConstraint(
            model_name='feedback',
            constraint=models.CheckConstraint(check=models.Q(('estimation__gte', 1), ('estimation__lte', 5)), name='estimation_range'),
        ),
    ]
