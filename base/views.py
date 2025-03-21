#create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer,PurchaseSerializer,SellSerializer,CostomerSerializer,VendorSerializer,DepartmentSerializer


class ProductApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PurchaseApiView(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class SellApiView(viewsets.ModelViewSet):
    querset= Sell.objects.all()
    serializer_class = SellSerializer

class CostomerApiView(viewsets.ModelViewSet):
    queryset=Coustumer.objects.all()
    serializer_class= CostomerSerializer

class VendorApiView(viewsets.ModelViewSet):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer

class DepartmentApiView(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer       