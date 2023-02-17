from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(user_register)
class Auth_User(admin.ModelAdmin):
    list_display =['id','user_first_name','user_last_name','user_age','user_phone','user_email','user_address','city','country','user_freelancer','user_bio','user_profile_picture','user_website','user_password','created_at','updated_at']

@admin.register(Education)
class UserEducation(admin.ModelAdmin):
    list_display=['id','Name_of_degree','city','country','start_date','end_date','created_at','updated_at','user_education']

@admin.register(professional_experiance)
class UserProfessionalExp(admin.ModelAdmin):
    list_display = ['id','Company_name','start_date','end_date','created_at','updated_at','user_company']

@admin.register(skills)
class Skills(admin.ModelAdmin):
    list_display = ['id','skill_name','grip_value','created_at','updated_at','user_skills']

@admin.register(Educative_achivements)
class Educative_achivement(admin.ModelAdmin):
    list_display = ['id','achivements_name','certification_link','certification_start_date','certification_end_date','created_at','updated_at','education']

@admin.register(professionl_achivements)
class professional_ahcivement(admin.ModelAdmin):
   list_display = ['id','achivements_name','certification_link','certification_start_date','certification_end_date','created_at','updated_at','p_achievement']

@admin.register(Company_skills)
class comp_skills(admin.ModelAdmin):
    list_display = ['id','skill_name','created_at','updated_at','p_skills']
