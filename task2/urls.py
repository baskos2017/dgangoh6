from django.urls import path
from . import views

urlpatterns = [
    path('filter_examples/', views.filter_examples, name='filter_examples'),
]
