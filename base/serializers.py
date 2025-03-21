from rest_framework import serializers
from .models import Product, Purchase, Sell, Vendor, Costomer, Department

class ProductSerializer(serializers.ModelSerializer):
    class meta:
        model=Product
        fields='__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class meta:
        model= Purchase 
        fields='__all__'

class SellSerializer(serializers.ModelSerializer):
    class meta:
        model= Sell
        fields='__all__'

class CostomerSerializer(serializers.ModelSerializer):
    class meta:
        model= Costomer
        fields='__all__'                   

class VendorSerializer(serializers.ModelSerializer):
    class meta:
        model= Vendor 
        fields='__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class meta:
        model= Department 
        fields='__all__'        
