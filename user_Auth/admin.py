from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(user_register)
class Users(admin.ModelAdmin):
    list_display =['id','user_first_name','user_last_name','user_age','user_phone','user_email','user_address','user_city','user_freelancer','user_bio','user_profile_picture','user_website','user_password']