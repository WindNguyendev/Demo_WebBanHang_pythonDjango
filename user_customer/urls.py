
from django.urls import path, include
from user_customer .views import SiteLoginView, EditProfileView, SiteRegisterOkView,SiteRegisterView,SiteLogoutView,Edit_profile,admin_1,Edit_product,manager_category,manager_product, Edit_category,manager_oder,Delete_product,Add_product,Delete_category,Add_category,manager_distributor,Add_distributor,Edit_distributor,Delete_distributor



urlpatterns = [
  
   path('logout', SiteLogoutView.as_view(), name='logout'),
   path('login', SiteLoginView.as_view(), name='login'),
   path('profile', EditProfileView.as_view(), name='profile'),
   path('register', SiteRegisterView.as_view(), name='register'),
   path('register/ok/', SiteRegisterOkView.as_view(), name='register_ok'),
   path('edit_profile',Edit_profile.as_view(), name='edit_profile'),

   path('admin_1',admin_1, name='admin_1'),
   path('edit_product/<int:pk>',Edit_product.as_view(), name='edit_product'),

   path('manager_category',manager_category, name='manager_category'),

   path('manager_product',manager_product, name='manager_product'),
   path('manager_distributor',manager_distributor, name='manager_distributor'),


   path('edit_category/<int:pk>',Edit_category.as_view(), name='edit_category'),
   path('edit_distributor/<int:pk>',Edit_distributor.as_view(), name='edit_distributor'),

   path('manager_order',manager_oder, name='manager_order'),

   path('delete_product/<int:pk>', Delete_product.as_view(), name = 'delete_product'),

   path('delete_category/<int:pk>', Delete_category.as_view(), name = 'delete_category'),
   path('delete_distributor/<int:pk>', Delete_distributor.as_view(), name = 'delete_distributor'),

   path('add_product', Add_product.as_view(), name = 'add_product'),
   path('add_category', Add_category.as_view(), name = 'add_category'),
   path('add_distributor', Add_distributor.as_view(), name = 'add_distributor'),


]
