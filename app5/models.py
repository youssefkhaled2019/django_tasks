from django.db import models

# Create your models here.

def content_file_name(instance, filename):  
    return "uploads/{folder}/{file}".format(id=instance, folder=instance.albumname, file=filename)


class Post(models.Model):
    title = models.CharField(max_length=200)    
    folder_name = models.CharField(max_length=50)    
    class Meta:
        ordering =["-id"]

class Data(models.Model):
    name_file = models.FileField(upload_to=content_file_name)
    albumname = models.CharField(max_length=100)
    type=models.IntegerField()
    size=models.IntegerField(null=type,blank=True)
    artcal=models.ForeignKey(Post,on_delete=models.CASCADE, related_name="data")    