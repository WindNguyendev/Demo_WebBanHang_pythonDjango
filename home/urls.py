from django.urls import path, include
from home .views import index, shop,aboutus, contact,productcat,productdetail,cart,history


urlpatterns = [
    path('',index,name='Trang Chu'),
    path('home/aboutus', aboutus, name='aboutus'),
    path('home/history', history, name='history'),
    path('home/shop', shop, name='shop'),
    path('home/contact', contact, name='contact'),
    path('home/shop/<int:id>', productcat, name='productcat'),
    path('home/productdetail/<int:id>', productdetail, name='productdetail'),
    path('home/cart',cart, name='cart'),
    path('home/login',cart, name='login'),
    

]
