"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user_customer import views
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin_tools_stats/', include('admin_tools_stats.urls')),#added this path
    path('admin_tools/', include('admin_tools.urls')),

    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('user_customer.urls')),
    path('', include('cart.urls')),
    path('', include('order.urls')),

    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)