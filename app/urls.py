from django.urls import path
from .views import index, about, FeedbackView, services

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('reviews/', FeedbackView.as_view(), name="reviews"),
    path('services/<str:type>', services, name="services"),
]