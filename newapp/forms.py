from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import Blog


class SignupForm(UserCreationForm):
    # password2= forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
        labels ={'email':'Email'}



class BlogForms(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['category','Title','Description','Image','Author']
        # widgets={"date":forms.DateTimeInput(format="%Y-%m-%d %H:%M:%S")}



class EditUserProfileForm(UserChangeForm):
    password = None 
    class Meta: 
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login'] 
        labels = {'email' : 'Email'}
