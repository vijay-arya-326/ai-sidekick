from django.urls import path
from .views import create_product, get_product, update_product, delete_product, list_products

urlpatterns = [
    path('products/', create_product),  # Create a product
    path('products/<int:product_id>/', get_product),  # Get a single product
    path('products/<int:product_id>/update/', update_product),  # Update a product
    path('products/<int:product_id>/delete/', delete_product),  # Delete a product
    path('products/all/', list_products),  # List all products
]