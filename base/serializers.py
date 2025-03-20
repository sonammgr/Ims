from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class meta:
        model=Product
        feilds='__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class meta:
        model= Purchase 
        feilds='__all__'

class SellSerializer(serializers.ModelSerializer):
    class meta:
        model= Sell
        feilds='__all__'            