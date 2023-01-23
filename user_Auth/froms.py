from django import forms
from .models import *
from django.core import validators
from phonenumber_field.formfields import PhoneNumberField

class User_registerations(forms.Form):
    user_first_name = forms.CharField(validators=[validators.MaxLengthValidator(30)],required=True)
    user_last_name = forms.CharField(required=True,validators=[validators.MaxLengthValidator(30)])
    user_age = forms.IntegerField(required=True,validators=[validators.MaxValueValidator(100)])
    user_phone = PhoneNumberField()
    user_email = forms.CharField(validators=[validators.EmailValidator()])
    user_address = forms.CharField(validators=[validators.MaxLengthValidator(255)])
    user_city = forms.CharField(validators=[validators.MaxLengthValidator(15)])
    user_freelancer = forms.BooleanField(required=True)
    user_bio = forms.CharField(required=True,validators=[validators.MaxLengthValidator(255)])
    # user_profile_picture = forms.ImageField(required=True)
    user_website = forms.URLField(required=True,validators=[validators.URLValidator()])
    user_password = forms.CharField(required=True,validators=[validators.RegexValidator("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",'Password is not Strong')])
    user_conf_password = forms.CharField(required=True,validators=[validators.RegexValidator("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",'Password is not Strong')])
    # class Meta:
    #     model = user_resgisteration
    #     fields = '__all__'