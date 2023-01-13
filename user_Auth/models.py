from django.db import models

# Create your models here.

class user_resgisteration(models.Model):
    user_first_name = models.CharField(max_length=30,blank=False,null=False)
    user_last_name = models.CharField(max_length=30,blank=False,null=False)
    user_age = models.IntegerField(max_length=3,blank=False,null=False)
    user_email = models.EmailField(null=False)
    user_address= models.TextField(null=False)
    user_city = models.CharField(max_length=15,null=False)
    user_freelancer = models.BooleanField()
    user_bio = models.TextField(max_length=255,null=False)
    user_profile_picture = models.ImageField(upload_to='image/',default=None)
    user_webstie = models.URLField()
    user_password = models.CharField(max_length=8)
    user_conf_password = models.CharField(max_length=8)

class user_images(models.Model):
    user = models.OneToOneField(user_resgisteration,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='/image')
    save_date = models.DateTimeField()
