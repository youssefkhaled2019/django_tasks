from django.shortcuts import render,redirect
from .models import Game
from .form import  GameForm


from django.conf import settings
import os
# Create your views here.
def index(request):
     game=Game.objects.all()
     context={"game":game,
              "form":GameForm}
     return render(request,'image_pdf_crud/index.html',context=context)





def add(request):
  
    if request.method=="POST":
       
       
        g=GameForm(request.POST, request.FILES)
        if g.is_valid():
           g.save()
           print("save ok")
           return redirect('home')

    else :
        print("ERROR")
    
    
    return render(request,'image_pdf_crud/index.html')


def update(request,id):
  
    if request.method=="POST":
       
       
        g=GameForm(request.POST, request.FILES)
        if g.is_valid():
           g.save()
           print("save ok")
           return redirect('home')

    else :
        print("ERROR")
    
    
    return render(request,'image_pdf_crud/index.html')

def delete(request,id):
  
    if request.method=="GET":
       
       
         game=Game.objects.get(id=id)
         

         #filepath =os.path.join(settings.MEDIA_ROOT,game.info.url)
         if(os.path.exists(game.info.path)):
             os.remove(game.info.path)
             os.remove(game.img.path)
             game.delete()
             print("delete ok")

         #print(str(settings.MEDIA_ROOT),str(filepath),str(game.info.path))   

         
         return redirect('home')


    else :
        print("ERROR")
    
    
    return render(request,'image_pdf_crud/index.html')


def search(request):
    if request.method=="GET":
        name=request.GET["name_search"]
        game=Game.objects.filter(name__contains=name)

        context={"game":game,
              "form":GameForm}
    return render(request,'image_pdf_crud/index.html',context)


def show_item(request ,id):
    if request.method=="GET":
        game=Game.objects.get(id=id)

    return render(request,'image_pdf_crud/item.html',context={"game":game})


def download(request,id):
    path=Game.objects.get(id=id).info

  
    print(path)
    return redirect('home')