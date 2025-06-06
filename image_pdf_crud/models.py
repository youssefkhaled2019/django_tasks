from django.db import models
from django.utils import timezone

# Create your models here.


import uuid
import os
import random
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename_start = filename.replace('.'+ext,'')
    filename  = "%s.%s"%(random.randint(1000, 10000) ,ext)  
    #filename = "%s__%s.%s" % (uuid.uuid4(),filename_start, ext)
    return os.path.join('pdf', filename)

class Game(models.Model):
    img=models.ImageField(upload_to="img/")
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    info=models.FileField(upload_to=get_file_path ,blank=True,null=True)

    # info=models.FileField(upload_to="pdf/",blank=True,null=True)
    dec=models.CharField(max_length=250,default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel assumenda ad nemo laudantium. Rem modi vitae adipisci magnam mollitia quos, maiores sit facere tempore dignissimos hic eaque, nesciunt voluptatibus. Facere.")
    date=models.DateTimeField(default=timezone.now)
    update=models.IntegerField(default=0)
    def __str__(self):
        return self.name