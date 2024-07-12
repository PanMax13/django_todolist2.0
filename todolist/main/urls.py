from django.urls import path
from . import views


patterns = [
    path('<slug:slug>/', views.filter_url, name='category'),
]


