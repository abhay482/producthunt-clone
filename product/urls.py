from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create, name='create' ),
    path('<int:product_id> details', views.detail, name='detail' ),
]