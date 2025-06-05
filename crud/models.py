from django.db import models
from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models  import User
from django.utils import timezone
# Create your models here.
class post(models.Model):
    text=models.TextField()
    n_update=models.IntegerField(default=0)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post_date=models.DateTimeField(default=timezone.now)#
    post_update_date=models.DateTimeField(auto_now=True)

    class Meta:
            ordering = ['-post_date']