from django.db import models
from home.models import Product

from django.contrib.auth.models import User

# Create your models here.



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.username}_Cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    size = models.IntegerField(default=37)


    
    def __str__(self):
        return f"{self.item.title}: {self.cart.user.username}" 
    

