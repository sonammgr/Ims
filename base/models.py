from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name=models.CharField(max_length=200)

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=400)
    price=models.FloatField()
    stock=models.IntegerField()
    catergory=models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True)
    department=models.ManyToManyField('Department')   

class Purchase(models.Model):
    product=models.ForeignKey('Product',on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.FloatField()
    vendor=models.ForeignKey('Vendor',on_delete=models.SET_NULL,null=True)

class Sell(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField()
    price=models.FloatField()
    costomer=models.ForeignKey('Costomer',on_delete=models.SET_NULL,null=True)

class Costomer(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    number=models.CharField(max_length=20)
    address=models.CharField(max_length=100)

class Vendor(models.Model):
    name=models.CharField(max_length=200)
    company_name=models.CharField(max_length=200)
    email=models.EmailField()
    number=models.CharField(max_length=20)
    company_address=models.CharField(max_length=200)
    
class Department(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=300)
    floor=models.IntegerField()      

