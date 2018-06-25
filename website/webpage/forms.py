__author__ = 'Mayank Sharma'
from django import forms

class Login(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)
        
class Signup(forms.Form):
    User_Name = forms.CharField(max_length=30)
    First_Name = forms.CharField(max_length=30)
    Last_Name = forms.CharField(max_length=30)
    Email = forms.EmailField(widget=forms.EmailInput)
    #Profile_Pic = forms.ImageField()
    Password = forms.CharField(max_length=30,widget=forms.PasswordInput)

