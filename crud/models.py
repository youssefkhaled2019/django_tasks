from django.db import models

# Create your models here.
from django.db import models
from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models  import User

# Create your models here.
class post(models.Model):
    text=models.CharField(max_length=50)
    n_update=models.IntegerField(default=0)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
