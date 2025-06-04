from django.db import models

# Create your models here.



class Artcals(models.Model):
    title = models.CharField(max_length=200)    
    class Meta:
        ordering =["-id"]

class Image(models.Model):
    pic = models.FileField(upload_to='Multiple_Images')
    artcal=models.ForeignKey(Artcals,on_delete=models.CASCADE,related_name="images" )    