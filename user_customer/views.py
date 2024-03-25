from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import EditUserProfileForm,Add_product_forms, Report
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from home.models import Product, Category, Distributor

from django.contrib import messages


from order.models import Order, Order_item
# Create your views here.
from django.http import HttpResponse

from django.core.paginator import Paginator

from cart.models import Cart, CartItem


def span_iconCart(request):
    try:
        us = request.user
        cart = Cart.objects.get(user=us)
        cart_item = CartItem.objects.filter(cart=cart)
        i = len(cart_item)
        return i

        
    except:
        pass




class SiteLoginView(LoginView):
    template_name = 'home/login.html'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget= forms.EmailInput(attrs={'data-id':2000}))
    class Meta:
        model = User
        fields = ('username','email')
        field_classes = {'username': UsernameField}

class SiteRegisterView(FormView):
    template_name = 'home/register.html'
    form_class = RegisterForm
    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(
            username=data['username'], 
            password=data['password1'],
            email=data['email']
            )
        url = f"{reverse('register_ok')}?username={new_user.username}"
        return redirect(url)
        
class SiteRegisterOkView(TemplateView):
    template_name = 'home/register_ok.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context            
        

class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'home/profile.html'
    
class SiteLogoutView(LogoutView):
    template_name = 'home/logout.html'
    

class Edit_profile(generic.UpdateView):

    form_class = EditUserProfileForm
    template_name = 'home/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


def admin_1(request):
    form = Report()
    i = span_iconCart(request)
    
    try:
        if request.method == 'POST':
            form = Report(request.POST)
            if form.is_valid:
                date_of_start = request.POST.get('date_of_start')
                date_of_last = request.POST.get('date_of_last')
        lst_pr = Order.objects.filter(created_at__gt='{}'.format(date_of_start),created_at__lt='{}'.format(date_of_last))
        # lst_pr_1 = Order.objects.filter(created_at__lt='{}'.format(date_of_last))   

        dic = {
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0
        }

        # dic_1 = {}

        # for i in lst_pr:
        #     if i.is_status == 3:
        #         order_item = Order_item.objects.filter(order = i)
        #         for y in order_item:
        #             if len(dic_1) == 0:
        #                 dic_1[y.name_pr] = int(y.quantity)
        #             else:    
        #                 for j in dic_1:
        #                     if j.keys() == y.name_pr:
        #                         dic_1[j.keys()] = dic_1[j.keys()] + y.quantity
        #                     else:
        #                         dic_1[y.name_pr] = int(y.quantity)
        # num = len(dic_1)

        # lst_quantity_item_order = []
        # for i in dic_1.values():
        #     lst_quantity_item_order.append(i)
        # max_quantity = max(lst_quantity_item_order)

        # lst_pr_1 = []

        # for i in dic_1.keys():
        #     if dic_1[i] == max_quantity:
        #         lst_pr_1.append(i)
        # lst_1 = {}
        # for i in lst_pr:
        #     if i.is_status == 3:
        #         order_item = Order_item.objects.filter(order = i)
        #         for j in order_item:
        #             if len(lst_1) ==0:
        #                 lst_1[j.name_pr] = i.quantity
        #             else:
        #                 for z in lst_1.keys():
        #                     if z == j.name_pr:
        #                         lst_1[z] = lst_1[z] + j.quantity
        #                     else:
        #                         lst_1[z] = j.quantity 
        # num = len(lst_1)

        total = 0
        for i in lst_pr:
            if(i.is_status == 3):
                total+= i.total


        for i in lst_pr:
            for j in dic.keys():
                if i.is_status == j:
                    dic[j] = dic[j] +1
        lst = []

        for i in dic.values():
            lst.append(i)





        return render(request,'home/admin_1.html',{'i':i,'lst':lst,'lst_pr':lst_pr,'form':form,'date_of_start':date_of_start,'date_of_last':date_of_last,'total':total})
    except:


        lst_pr = Order.objects.all()
        return render(request,'home/admin_1.html',{'i':i,'lst_pr':lst_pr,'form':form})

class Edit_product(UpdateView):
    model = Product
    fields = "__all__"
    template_name = 'home/edit_product.html'
    success_url = "/manager_product"


def manager_category(request):
    list_category = Category.objects.all()
    i= span_iconCart(request)
    return render(request,'home/manager_category.html',{'i':i,'list_category':list_category})

def manager_distributor(request):
    try:
        d = request.GET.get('d')
        list_distributor = Distributor.objects.filter(title__icontains=d)
    except:
        list_distributor = Distributor.objects.all()
    i=span_iconCart(request)
    return render(request,'home/manager_distributor.html',{'i':i,'list_distributor':list_distributor})


def manager_product(request):
    i = span_iconCart(request)
    try:

        s =request.GET.get('p')
        lst_pr = Product.objects.filter(title__icontains=s)
    except:
        lst_pr = Product.objects.all()

    paginator = Paginator(lst_pr, 6) # Show 25 contacts per page

    page = request.GET.get('page')
    lst_pr = paginator.get_page(page)
    return render(request,'home/manager_product.html',{'i':i,'lst_pr':lst_pr})

    
class Edit_category(UpdateView):
    model = Category
    fields = "__all__"
    template_name = 'home/edit_category.html'
    success_url = "/manager_category"


class Edit_distributor(UpdateView):
    model = Distributor
    fields = "__all__"
    template_name = 'home/edit_distributor.html'
    success_url = "/manager_distributor"

def manager_oder(request):

    i = span_iconCart(request)
    try:

        o =request.GET.get('o')
        lst_oder = Order.objects.filter(name__icontains=o)
        lst_oder = lst_oder[::-1]
    except:
        lst_oder = Order.objects.all()
        lst_oder = lst_oder[::-1]
    order_item = Order_item.objects.all()




    return render(request,'home/manager_order.html',{'i':i,'lst_oder':lst_oder,'order_item':order_item})


class Delete_product(DeleteView):
    model = Product
    success_url ="/manager_product"
    template_name = "home/delete_product.html"

class Delete_distributor(DeleteView):
    model = Distributor
    success_url ="/manager_distributor"
    template_name = "home/delete_distributor.html"

class Delete_category(DeleteView):
    model = Category
    success_url ="/manager_category"
    template_name = "home/delete_category.html"


class Add_product(CreateView):
    form_class = Add_product_forms
    template_name = "home/add_product.html"
    success_url = reverse_lazy('manager_product')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(Add_product,self).form_valid(form)


class Add_category(CreateView):
    model = Category
    fields = '__all__'
    template_name = "home/add_product.html"
    success_url = reverse_lazy('manager_category')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(Add_category,self).form_valid(form)

class Add_distributor(CreateView):
    model = Distributor
    fields = '__all__'
    template_name = "home/add_distributor.html"
    success_url = reverse_lazy('manager_distributor')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(Add_distributor,self).form_valid(form)
        
        
