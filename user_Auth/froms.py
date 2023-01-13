from django import forms
from .models import *
from django.core import validators

class User_registerations(forms.ModelForm):
    First_Name = forms.CharField(widget=forms.TextInput(),blank=False, null=False,validators=[validators.MaxLengthValidator(30)])
    Last_Name = forms.CharField(widget=forms.TextInput(),blank=False, null=False,validators=[validators.MaxLengthValidator(30)])
    age = forms.IntegerField(widget=forms.IntegerField(),blank=True, null=False,validators=[validators.MaxValueValidator(100)])
    email = forms.CharField(widget=forms.EmailInput(),validators=[validators.EmailValidator()])
    phone = forms.CharField(widget=forms)
    password = forms.CharField(widget=forms.PasswordInput(),validators=[validators.RegexValidator("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",'Password is not Strong'),validators.MaxLengthValidator(9)])
    confirm_password = forms.CharField(widget=forms.PasswordInput(),validators=[validators.RegexValidator("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",'Password is not Strong'),validators.MaxLengthValidator(9)])
    address = forms.CharField(widget=forms.Textarea(),validators=[validators.MaxLengthValidator(255)])
    city = forms.CharField(widget=forms.TextInput(),validators=[validators.MaxLengthValidator(15)])
    freelancer = forms.BooleanField(widget=forms.BooleanField(),validators=[validators.MaxValueValidator(1)])
    bio = forms.CharField(widget=forms.Textarea(),validators=[validators.MaxLengthValidator(255)])
    profile_picture = forms.ImageField(widget=forms.ImageField(required=True))
    web_url = forms.URLInput()

    class Meta:
        model = user_images
        model  = user_resgisteration
        fields = ['First_Name','Last_Name','email','password','confirm_password','age','address','city','freelancer','bio','image']