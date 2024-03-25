from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Category, Product, Product_Featured
from django.contrib.auth.decorators import login_required
from cart.models import Cart,CartItem
from django.contrib.auth.models import User
from order.models import Order, Order_item
from order.forms import PostOrder
from django.core.paginator import Paginator


# Create your views here.

def span_iconCart(request):
    try:
        us = request.user
        cart = Cart.objects.get(user=us)
        cart_item = CartItem.objects.filter(cart=cart)
        i = len(cart_item)
        return i

        
    except:
        pass


def index(request):
    try:
        us = request.user
        cart = Cart.objects.get(user=us)
        cart_item = CartItem.objects.filter(cart=cart)
        i = len(cart_item)

        return render(request,'home/index.html',{'i':i})

        
    except:
        return render(request,'home/index.html')

def aboutus(request):
    i= span_iconCart(request)
    list_product = Product.objects.filter(active =True)
    return render(request,'home/aboutus.html',{'list_product':list_product,"i":i})


def shop(request):
    try:
        s =request.GET.get('s')
        list_product = Product.objects.filter(title__icontains=s)
        list_category = Category.objects.all()
        
    except:
        list_category = Category.objects.all()
        list_product = Product.objects.filter(active =True)

    paginator = Paginator(list_product, 6) # Show 25 contacts per page

    page = request.GET.get('page')
    list_product = paginator.get_page(page)
        
    return render(request,'home/shop.html',{'list_category':list_category,
                                            'list_product':list_product,
                                            "i":span_iconCart(request)})




def contact(request):
    return render(request,'home/contact.html',{"i":span_iconCart(request)})

def productcat(request,id):
    category_id = Category.objects.get(id = id)
    list_productcat = Product.objects.filter(category=category_id)
    list_category = Category.objects.all()
    paginator = Paginator(list_productcat, 6) # Show 25 contacts per page

    page = request.GET.get('page')
    list_productcat = paginator.get_page(page)

    return render(request,'home/productcat.html',{'list_category':list_category,
                                                'productcat':list_productcat,
                                                "i":span_iconCart(request)})

def productdetail(request,id):
    try:
        us = request.user
        try:
            cart = Cart.objects.get(user=us)
        except:
            cart = Cart(user=us)
            cart.save()
        list_cartItems = CartItem.objects.filter(cart=cart)
        for i in list_cartItems:
            if i.item.id == id:
                quantity = int(i.quantity)
        detail = Product.objects.get(id=id)
        product_Featured = Product_Featured.objects.all()
        return render(request,'home/productdetail.html',{'detail':detail,
                                                         'quantity':quantity,
                                                        'product_Featured':product_Featured,
                                                        "i":span_iconCart(request)})
        

    except:

        detail = Product.objects.get(id=id)
        product_Featured = Product_Featured.objects.all()
    
        return render(request,'home/productdetail.html',{'detail':detail,
                                                        'product_Featured':product_Featured,
                                                        "i":span_iconCart(request)})

@login_required
def cart(request):

    order_forms = PostOrder()

    try:
        
        us = request.user
        try:
            cart = Cart.objects.get(user=us)
        except:
            cart = Cart(user=us)
            cart.save()
        list_cartItems = CartItem.objects.filter(cart=cart)
        total = 0
        for i in list_cartItems:
            total += i.quantity*i.item.price

        return render(request,'home/cart.html',{'list_cartItems':list_cartItems,
                                                "i":span_iconCart(request),
                                                'total':total,
                                                'order_forms':order_forms})
    except:
        return render(request,'/',{"i":span_iconCart(request)})


@login_required
def history(request):
    us = request.user
    order = Order.objects.filter(user=us)
    order = order[::-1]
    order_item = Order_item.objects.all()




            


    return render(request,'home/history.html',{'order':order,'order_item':order_item,
                                               'i':span_iconCart(request)})
    