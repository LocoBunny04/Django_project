from django.urls import path

from . import views

# Create your URL paths here.

urlpatterns = [
    path('', views.index, name='index'),
    ]