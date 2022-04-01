from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from products import serializers


@api_view(['GET', 'POST'])
def all_products(request):
    if request.method == 'GET':
        query_set = Product.objects.all()
        serializer = ProductSerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def single_product(request, pk):
    query_set= get_object_or_404(Product,pk=pk)
    if request.method == 'GET':
        serializer = ProductSerializer(query_set)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializer(query_set, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        query_set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
