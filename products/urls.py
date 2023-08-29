from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_products),
    path('product/<str:name>/', views.get_product),
    path('create-product/', views.create_product),
    path('edit-product/<int:pk>/', views.edit_product),
    path('delete-product/<int:pk>/', views.delete_product)
]
