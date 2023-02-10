from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.manager import Manager

# Create your models here.

class BaseCreatedAtModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)
    city = models.CharField(max_length=30,blank=False,null=True)
    country = models.CharField(max_length=30,blank=False,null=True)
    class Meta:
        abstract = True

class BaseStartAtEndAt(models.Model):
    start_date = models.DateField(blank=False,null=True)
    end_date = models.DateField(blank=False,null=True)
    class Meta:
        abstract = True

class BaseAchivementsModel(models.Model):
    achivements_name = models.CharField(max_length=30)
    certification_link = models.URLField(null=True)
    certification_start_date = models.DateField(null=True)
    certification_end_date = models.DateField(null=True)
    achivements = models.Manager()
    class Meta:
        abstract = True

class BaseSkillsModel(models.Model):
    skill_name = models.CharField(max_length=30,null=True)
    grip_value = models.SmallIntegerField(blank=False,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)
    class Meta:
        abstract = True
        

        
class user_register(models.Model):
    login_check = models.BooleanField(blank=True)
    user_first_name = models.CharField(max_length=30,blank=False, null=True)
    user_last_name = models.CharField(max_length=30,blank=False,null=True)
    user_age = models.IntegerField(blank=False,null=True)
    user_phone = PhoneNumberField()
    user_email = models.EmailField(blank=False,null=True)
    user_address= models.TextField(blank=False,null=True)
    user_city = models.CharField(max_length=15,blank=False,null=True)
    user_freelancer = models.BooleanField(blank=True)
    user_bio = models.TextField(max_length=255,blank=False,null=True)
    user_profile_picture = models.ImageField(upload_to='image/%y',blank=False,default=None)
    user_website = models.URLField()
    user_password = models.CharField(max_length=9,blank=False,null=True)
    registration = models.Manager()

class Education(BaseStartAtEndAt,BaseCreatedAtModel):
    user = models.ForeignKey(user_register, verbose_name=("USER_ID"), on_delete=models.CASCADE)
    Name_of_degree = models.CharField(max_length=30,blank=False,null=True)
    Education_data = models.Manager()

class skills(BaseSkillsModel):
    user_skills = models.ForeignKey(user_register,verbose_name=('User_id'),on_delete=models.CASCADE)
    skills = models.Manager()

class professional_experiance(BaseStartAtEndAt,BaseCreatedAtModel):
    user_company = models.ForeignKey(user_register,verbose_name=('User_id'),on_delete=models.CASCADE)
    Company_name = models.CharField(max_length=30 , blank=False,null=True)
    prof_exp = models.Manager()

class Educative_achivements(BaseAchivementsModel):
    education = models.ForeignKey(Education, verbose_name=("education_id"), on_delete=models.CASCADE)
    edu_achivements = models.Manager()

class professionl_achivements(BaseAchivementsModel):
    p_achievements = models.ForeignKey(professional_experiance,verbose_name=('p_exp_id'), on_delete=models.CASCADE)
    p_achievements = models.Manager()

class Company_skills(BaseSkillsModel):
    p_skills = models.ForeignKey(professional_experiance,verbose_name=('Prof_exp_id'),on_delete=models.CASCADE)
    prof_skill = models.Manager()












