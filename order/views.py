from django.shortcuts import render
from .forms import PostOrder
from .models import Order,Order_item
from cart.models import Cart, CartItem
from home.models import Product
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

# Create your views here.


def Order_new(request):
    if request.method == 'POST':
        o = PostOrder(request.POST)
        if o.is_valid:
            us = request.user
            cart = Cart.objects.get(user=us)

            
            cart_item = CartItem.objects.filter(cart=cart)
            total = 0
            for i in cart_item:
                total += i.quantity*i.item.price


            order_new = Order(user = us,name= request.POST.get('name'),total = total,phone= request.POST.get('phone'),shiping_address= request.POST.get('shiping_address'),order_description= request.POST.get('order_description'),)

            order_new.save()



            Prct = Product.objects.filter(active =True)
            for i in cart_item:
                for j in Prct:
                    if i.item == j:
                        Prct_edit = Product.objects.get(id = j.id)
                        Prct_edit.quantity_stock = Prct_edit.quantity_stock - i.quantity
                        Prct_edit.save()
                
            for i in  cart_item:  
                order_item_new = Order_item(order = order_new,name_pr=i.item.title,quantity=i.quantity,total=int(i.item.price)*int(i.quantity),product_img=i.item.product_img)
                order_item_new.save()
                i.delete()

               

                

            return render(request,"home/successfully_order.html")
        else:
            return HttpResponse("Nhập không đúng dữ liệu")
    else:
        return HttpResponse("Không phải request kiểu POST")


    

def remove_oder(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        id = request.POST.get('id')
        order = Order.objects.get(id=id)
        order.is_status = 4
        order.save()
        order_item = Order_item.objects.filter(order = order)
        for i in order_item:
            product_get = Product.objects.get(title=i.name_pr)
            product_get.quantity_stock = product_get.quantity_stock + i.quantity
            product_get.save()
        
        html = render_to_string('home/remove_order.html')
    return HttpResponse(html)

def return_oder(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        id = request.POST.get('id')
        order = Order.objects.get(id=id)
        order.is_status = 5
        order.save()
        html = render_to_string('home/return_order.html')
    return HttpResponse(html)


def done_oder(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        id = request.POST.get('id')
        order = Order.objects.get(id=id)
        order.is_status = 3
        order.save()
        html = render_to_string('home/done_order.html')
    return HttpResponse(html)

def approve_orders(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        id = request.POST.get('id')
        order = Order.objects.get(id=id)
        order.is_status = 1
        order.save()
        html = render_to_string('home/done_order.html')
    return HttpResponse(html)

def admin_remove_order(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        id = request.POST.get('id')
        order = Order.objects.get(id=id)
        order.is_status = 6
        order.save()
        order_item = Order_item.objects.filter(order = order)
        for i in order_item:
            product_get = Product.objects.get(title=i.name_pr)
            product_get.quantity_stock = product_get.quantity_stock + i.quantity
            product_get.save()
        html = render_to_string('home/admin_remove_order.html')
    return HttpResponse(html)

def admin_delivery_order(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        id = request.POST.get('id')
        order = Order.objects.get(id=id)
        order.is_status = 2
        order.save()
        html = render_to_string('home/done_order.html')
    return HttpResponse(html)


