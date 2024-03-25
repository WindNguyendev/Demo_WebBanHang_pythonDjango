
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from home.models import Product
from .models import Cart,CartItem
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def addcart(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest': 
        id_pr = request.POST.get('id_pr')
        id_us = request.POST.get('id_us')
        num = request.POST.get('num')
        size = request.POST.get('size')

        us = request.user
        pr = Product.objects.get(id=id_pr)

        try:
            cart = Cart.objects.filter(user=us)
            if len(cart) == 0:
                cart_new = Cart(user=us)
                cart_new.save()
            else:
                for i in cart:
                    cart_new =i
            
        except:
            pass
        
        cart_items = CartItem.objects.filter(cart=cart_new,item=pr)
        if len(cart_items) == 0:
            cart_items_new = CartItem(cart=cart_new,item =pr,quantity=int(num),size=int(size))
            cart_items_new.save()
        else:
            cart_items_new = CartItem.objects.get(cart=cart_new,item=pr,size=int(size))
            cart_items_new.quantity= int(num)+ int(cart_items_new.quantity)
            cart_items_new.save()


        html = render_to_string('home/addcart.html')
    return HttpResponse(html)


def edit_quantity_1(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        id = request.POST.get('id_citem')
        id_edit = request.POST.get('id_edit')
        tonkho = request.POST.get('tonkho')
        cart_item = CartItem.objects.get(id=id)
        if id_edit == "1":
            cart_item.quantity = cart_item.quantity -1
            if cart_item.quantity == 0:
                cart_item.delete()
            else:
                cart_item.save()
            html = render_to_string('home/edit_quantity_1.html')
        elif id_edit == "2":
            cart_item.quantity = cart_item.quantity +1
            cart_item.save()
            html = render_to_string('home/edit_quantity_1.html')
        else:
            cart_item.delete()
            html = render_to_string('home/edit_quantity_1.html')


    return HttpResponse(html)


    
