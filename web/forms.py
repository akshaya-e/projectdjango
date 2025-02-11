from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.forms import User


#DJANGO FORM

class EnquiryForm(forms.Form):
    name=forms.CharField(label='your name',max_length=100)
    email=forms.EmailField(label='Email')
    message=forms.CharField(label='your msg',widget=forms.Textarea)
    
#MODEL FORM
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','age','ad_num','department']
        
class UserRegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=100)
    
    class Meta:
        model= User
        fields= ['first_name','username','email']
        
class UserLoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']
        
class BooksForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=['title','pub_date','author','image','fl']
