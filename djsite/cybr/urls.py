from django.urls import path

from . import views

# Create your URL paths here.

urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path('', views.home, name='home'),
    ]