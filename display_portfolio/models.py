from django.db import models

# Create your models here.

class User_Education(models.Model):
    name_of_degree = models.CharField(max_length=15,null=False)
    start_of_degree = models.DateField(null=False)
    end_of_degree = models.DateField(null=False)
    degree_city = models.CharField(max_length=15, null=False)
    degree_country = models.TextField(max_length=15,null=False)
