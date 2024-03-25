from .models import Order
from django import forms
from django.contrib.auth.models import User






class PostOrder(forms.ModelForm):
    
    class Meta():
        model = Order
        fields = ['name', 'phone', 'shiping_address','order_description',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','type': 'text', 'placeholder':'Họ tên'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','type': 'tel', 'placeholder':'Số điện thoại'}),
            'shiping_address': forms.TextInput(attrs={'class': 'form-control','type': 'text', 'placeholder':'Địa chỉ'}),
            'order_description': forms.TextInput(attrs={'name':'c_message','class': 'form-control','type': 'text', 'placeholder':'Ghi chú','cols':'30','rows':'7','id':'c_message'}),
        }



