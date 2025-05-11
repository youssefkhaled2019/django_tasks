from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="photos/%y/%m/%d",default='0.jpg')