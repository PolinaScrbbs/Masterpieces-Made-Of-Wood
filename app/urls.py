from django.urls import path
from .views import index, about, reviews, services

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('reviews/', reviews, name="reviews"),
    path('services/<str:type>', services, name="services"),
]