from django.urls import path, include
from  .views import Order_new,remove_oder, return_oder, done_oder,approve_orders,admin_remove_order,admin_delivery_order


urlpatterns = [
    
    path('home/order', Order_new, name='order'),
    path('home/remove_order', remove_oder, name='remove_oder'),
    path('home/return_order', return_oder, name='return_oder'),
    path('home/done_order', done_oder, name='done_oder'),
    path('home/approve_orders', approve_orders, name='approve_orders'),
    path('home/admin_remove_order', admin_remove_order, name='admin_remove_order'),
    path('home/admin_delivery_order', admin_delivery_order, name='admin_delivery_order'),
    
   

]
