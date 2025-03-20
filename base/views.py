#create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PurchaseApiView(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class SellApiView(viewsets.ModelViewSet):
    querset= Sell.objects.all()
    serializer_class = SellSerializer

