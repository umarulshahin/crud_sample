from django.db import models

# Create your models here.

class movie_info(models.Model):
    Name=models.CharField(max_length=250, default="Default Name")
    Year=models.IntegerField(null=True)
    discription=models.TextField()
    
class movie_details(models.Model):
    Name=models.CharField(max_length=250 )
    Year=models.IntegerField(null=True)
    discription=models.TextField()