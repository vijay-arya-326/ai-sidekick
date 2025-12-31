from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Product
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
@api_view(['POST'])
def create_product(request):
    data = json.loads(request.body)
    product = Product.objects.create(
        name=data['name'],
        description=data.get('description', ''),  # Optional description
        price=data['price'],
        is_active=data['is_active']
    )
    return JsonResponse({'id': product.id}, status=201)

@csrf_exempt
@api_view(['GET'])
def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return JsonResponse({'id': product.id, 'name': product.name, 'description': product.description, 'price': str(product.price), 'is_active': product.is_active})

@csrf_exempt
@api_view(['PUT'])
def update_product(request, product_id):
    data = json.loads(request.body)
    product = Product.objects.get(id=product_id)
    product.name = data['name']
    product.description = data.get('description', product.description)  # Optional description
    product.price = data['price']
    product.is_active = data['is_active']
    product.save()
    return JsonResponse({'id': product.id})

@csrf_exempt
@api_view(['DELETE'])
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return JsonResponse({'message': 'Product deleted'}, status=204)

@csrf_exempt
@api_view(['GET'])
def list_products(request):
    products = Product.objects.all()  # Get all products
    product_list = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": str(product.price),
            "is_active": product.is_active,
            "url": f"http://127.0.0.1:8000/v1/products/{product.id}/"  # URL for each product
        }
        for product in products
    ]
    return JsonResponse(product_list, safe=False)  # Return list of products as JSON
