from django.db import models
from cart.models import Cart
from django.contrib.auth.models import User


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default="", null=False)
    phone = models.CharField(max_length=10,default="",null=False)
    shiping_address = models.CharField(max_length=255, default='',null=False)
    order_description = models.TextField(default='')
    total = models.IntegerField(default=0)
    is_status= models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return f"{self.user.username}:{self.name}"

class Order_item(models.Model):
    order = models.ForeignKey(Order, on_delete= models.CASCADE)
    name_pr = models.CharField(max_length=100,default="", null=True)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    product_img = models.ImageField(null=True)
    def __str__(self) :
        return f"{self.name_pr}"



