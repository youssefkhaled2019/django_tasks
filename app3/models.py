from django.db import models

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=200)    

class Data(models.Model):
    name_file = models.FileField(upload_to='data')
    type=models.IntegerField()
    size=models.IntegerField(null=type,blank=True)
    artcal=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="data" )    