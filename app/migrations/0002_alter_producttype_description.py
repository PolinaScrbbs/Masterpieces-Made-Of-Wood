# Generated by Django 5.0.6 on 2024-06-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='description',
            field=models.TextField(max_length=150, verbose_name='Описание'),
        ),
    ]
