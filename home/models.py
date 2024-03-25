from django.db import models

# Create your models here.

class Distributor(models.Model):
    title = models.CharField(max_length=255,default='')
    email = models.EmailField(max_length = 200, null = False)
    phone = models.CharField(max_length=12, null = False)
    address = models.CharField(max_length=255, null = False)
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255,default='')
    distributor = models.ForeignKey(Distributor,null = True,on_delete=models.PROTECT)
    slup = models.CharField(max_length=100,default='')
    description = models.TextField(default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255,default='')
    description = models.TextField(default='')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    #product_img = models.CharField(max_length=255,default='')
    product_img = models.ImageField(null=True)
    quantity_stock = models.IntegerField(null=True)
    price = models.IntegerField(default=0,null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product_Featured(models.Model):
    title = models.CharField(max_length=255,default='')
    description = models.TextField(default='')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_img = models.CharField(max_length=255,default='')
    price = models.IntegerField(default=0,null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title




    