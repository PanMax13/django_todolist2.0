from django.urls import path
from . import views

login_urlpatterns = [
    path('', views.login),
    path('greeting/', views.greeting)
]