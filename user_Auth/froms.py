from django import forms
from .models import *
from django.core import validators

class User_registerations(forms.Form):
    user_first_name = forms.CharField(widget=forms.TextInput(),required=True,validators=[validators.MaxLengthValidator(30)])
    user_last_name = forms.CharField(widget=forms.TextInput(),required=True,validators=[validators.MaxLengthValidator(30)])
    user_age = forms.IntegerField(widget=forms.NumberInput(),required=True,validators=[validators.MaxValueValidator(100)])
    user_phone = forms.IntegerField(widget=forms.NumberInput(),validators=[validators.MaxLengthValidator(15)])
    user_email = forms.CharField(widget=forms.EmailInput(),validators=[validators.EmailValidator()])
    user_address = forms.CharField(widget=forms.Textarea(),validators=[validators.MaxLengthValidator(255)])
    user_city = forms.CharField(widget=forms.TextInput(),validators=[validators.MaxLengthValidator(15)])
    user_freelancer = forms.BooleanField(required=True)
    user_bio = forms.CharField(widget=forms.Textarea(),validators=[validators.MaxLengthValidator(255)])
    user_profile_picture = forms.ImageField(required=True)
    user_website = forms.URLField(widget=forms.URLInput(),validators=[validators.URLValidator()])
    user_password = forms.CharField(widget=forms.PasswordInput(),validators=[validators.RegexValidator("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",'Password is not Strong'),validators.MaxLengthValidator(9)])
    user_conf_password = forms.CharField(widget=forms.PasswordInput(),validators=[validators.RegexValidator("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",'Password is not Strong'),validators.MaxLengthValidator(9)])

    # class Meta:
    #     model  = user_resgisteration
    #     fields = '__all__'