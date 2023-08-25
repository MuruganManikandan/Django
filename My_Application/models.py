from django.db import models

# Create your models here.
class Datas(models.Model):
    Name=models.CharField(max_length=20,default="")
    mail=models.CharField(max_length=60,default="")
    number=models.IntegerField(default="")
    msg=models.CharField(max_length=500,default="")