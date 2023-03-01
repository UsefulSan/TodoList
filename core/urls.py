from django.urls import path
from core import views

urlpatterns = [
    path('sign-up/', views.UserCreate.as_view()),
]