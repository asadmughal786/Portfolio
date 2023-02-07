from django import forms
from .models import *
from django.core import validators
from phonenumber_field.formfields import PhoneNumberField

class User_registerations(forms.Form):
    user_profile_picture = forms.ImageField(required=True)
    user_first_name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'First Name'}),validators=[validators.MaxLengthValidator(30)],required=True)
    user_last_name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Last Name'}),validators=[validators.MaxLengthValidator(30)],required=True,)
    user_age = forms.IntegerField(label='Age',widget=forms.NumberInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Age'}),validators=[validators.MaxValueValidator(100)],required=True)
    user_phone = PhoneNumberField(label='Phone Number',widget=forms.NumberInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Phone Numbers'}))
    user_email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'email@gmail.com'}),validators=[validators.EmailValidator()])
    user_city = forms.CharField(label='City',widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'City'}),validators=[validators.MaxLengthValidator(15)])
    user_website = forms.URLField(label='Website URL',widget=forms.URLInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'https://www.google.com'}),validators=[validators.URLValidator()],required=True)
    user_password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Password'}),validators=[validators.RegexValidator("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",'Password is not Strong')],required=True)
    user_conf_password = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Confirm Password'}),validators=[validators.RegexValidator("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",'Password is not Strong')],required=True)
    user_address = forms.CharField(label='Address',widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Address'}),validators=[validators.MaxLengthValidator(255)])
    user_bio = forms.CharField(label='Bio',widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Bio'}),validators=[validators.MaxLengthValidator(255)],required=True,)
    user_freelancer = forms.BooleanField(widget=forms.CheckboxInput(),required=True)

class User_Login(forms.Form):
    login_email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Enter Email'}),validators=[validators.EmailValidator()],required=True)
    login_pass = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),validators=[validators.RegexValidator("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",'Password is not Strong')],required=True)
