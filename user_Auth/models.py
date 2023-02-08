from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class user_register(models.Model):
    user_first_name = models.CharField(max_length=30,blank=False, null=True)
    user_last_name = models.CharField(max_length=30,blank=False,null=True)
    user_age = models.IntegerField(blank=False,null=True)
    user_phone = PhoneNumberField()
    user_email = models.EmailField(blank=False,null=True)
    user_address= models.TextField(blank=False,null=True)
    user_city = models.CharField(max_length=15,null=True)
    user_freelancer = models.BooleanField(blank=True)
    user_bio = models.TextField(max_length=255,null=True)
    user_profile_picture = models.ImageField(upload_to='image/%y',default=None)
    user_website = models.URLField()
    user_password = models.CharField(max_length=9,null=False)