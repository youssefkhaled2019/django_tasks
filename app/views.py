from django.shortcuts import render
from django.http import HttpResponse
from .models import  post
# Create your views here.
def index(request):
    # return HttpResponse("ffffffffffff")
    data=post.objects.all()
    return render(request,"index.html",{"data":data})