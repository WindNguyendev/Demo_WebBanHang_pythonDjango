from django.urls import path, include
from  .views import addcart, edit_quantity_1


urlpatterns = [
    
    path('home/addcart', addcart, name='addcart'),
    path('home/editquantity_1', edit_quantity_1, name='editquantity_1'),
    
   

]
