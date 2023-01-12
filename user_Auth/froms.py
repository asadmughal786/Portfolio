from django import forms
from .models import user_resgisteration
from django.core import validators

class User_registerations(forms.ModelForm):
    First_Name = forms.CharField(widget=forms.TextInput(),blank=False, null=False,validators=[validators.MaxLengthValidator(30,'Max Characters Limit exceeded')])
    Last_Name = forms.CharField(widget=forms.TextInput(),blank=False, null=False,validators=[validators.MaxLengthValidator(30,'Max Characters Limit exceeded')])
    age = forms.IntegerField(widget=forms.IntegerField(),blank=True, null=False,validators=[validators.MaxValueValidator(100)])
    email = forms.CharField(widget=forms.EmailInput(),validators=[validators.EmailValidator()])
    phone = forms.CharField(widget=forms)
    password = forms.CharField(widget=forms.PasswordInput(),validators=[validators.RegexValidator("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",'Password is not Strong'),validators.MaxLengthValidator(9,'Only 9 characters are Allowed to input')])
    confirm_password = forms.CharField(widget=forms.PasswordInput(),validators=[validators.RegexValidator("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",'Password is not Strong'),validators.MaxLengthValidator(9,'Only 9 characters are Allowed to input')])
    address = forms.CharField(widget=forms.Textarea(),validators=[validators.MaxLengthValidator(255,"Max Characters Limit exceeded")])
    city = forms.CharField(widget=forms.TextInput(),validators=[validators.MaxLengthValidator(15,'Max Characters Limit exceeded')])
    freelancer = forms.BooleanField(widget=forms.BooleanField(),validators=[validators.MaxValueValidator(1,'Please select Available or Not Available')])
    bio = forms.CharField(widget=forms.Textarea(),validators=[validators.MaxLengthValidator(255,'You can only write 255 characters')])
    profile_picture = forms.ImageField(widget=forms.ImageField(required=True))
    web_url = forms.URLInput(None,None,'Please enter the Url with Http","Https "," ftp "," ftps')

    class Meta:
        model  = user_resgisteration
        fields = ['First_Name','Last_Name','email','password','confirm_password','age','address','city','freelancer','bio','profile_picture']