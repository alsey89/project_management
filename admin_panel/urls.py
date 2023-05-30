from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_organization/', views.create_organization, name='create_organization'),
]
