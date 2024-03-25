from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm
from django import forms
from home.models import Product


class EditUserProfileForm(UserChangeForm):
	email = forms.EmailField(widget = forms.EmailInput(attrs= {'class': 'form-control','placeholder':"Enter your email"}))
	first_name = forms.CharField(widget = forms.TextInput(attrs= {'class': 'form-control','placeholder':"Enter your first name"}))
	last_name = forms.CharField(widget = forms.TextInput(attrs= {'class': 'form-control','placeholder':"Enter your last name"}))
	username = forms.CharField(max_length = 100,widget = forms.TextInput(attrs= {'class': 'form-control','placeholder':"Enter your last name"}))

	class Meta:
		model = User
		fields = ('username','first_name','last_name', 'email',)








class Add_product_forms(forms.ModelForm):
    
    class Meta():
        model = Product
        fields = '__all__'
       


from django.forms.widgets import NumberInput  
class Report(forms.Form):  
    date_of_start = forms.DateField(widget = NumberInput(attrs={'type':'date'})) 
    date_of_last = forms.DateField(widget = NumberInput(attrs={'type':'date'})) 
