from django.shortcuts import render,redirect
from .forms import PostForm,UserRegisterForm
from .models import post
from django.contrib import messages

# from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login') #redirect when user is not logged in
def home(request):
    

    if request.method=="POST":
       form= PostForm(request.POST )
       if(form.is_valid()):
        #    form.save(request.user)
           obj = form.save(commit=False)
           obj.author = request.user
           obj.save()
           return redirect("home")
    else:
       data=post.objects.all()
       form=PostForm()  
      
    cotext={ "type":"add",
             "form":form,
             "data":data}   
    return render(request ,"crud/home.html",cotext)     

def update(request,id):
    data=post.objects.get(id=id)
    if request.method=="POST":
       print(request.POST)
       form= PostForm(request.POST,instance=data)
       if(form.is_valid() and data.author == request.user ):
          
        #    form.save()
        #    data.n_update+=1
        #    data.save()
           data.text=form.cleaned_data["text"]
           data.n_update+=1
           data.save()


           return redirect("home")
    form= PostForm(instance=data)   
    cotext={"type":"update","form1":form}     
    return render(request ,"crud/home.html",cotext)    

def delete(request,id):
    post_= post.objects.get(id=id)
    if(post_.author == request.user ):
      post.objects.get(id=id).delete()
      return redirect("home")

# def login(request):
#         return render(request ,"login.html")    



def search(request):
   data_=post.objects.filter(text__contains=request.GET["search"])
   form=PostForm()  
   cotext={"type":"add",
        "form":form,
            "data":data_}   
   return render(request ,"crud/home.html",cotext)    



def register (request):
    if request.method=="POST":
       form= UserRegisterForm(request.POST)
       if form.is_valid():
          
          form.save()
          usename=form.cleaned_data.get("username")
          messages.success(request ,f'account created for {usename}')
          return redirect("home")
    else:
          form=UserRegisterForm()

    
    return render(request, "crud/register.html",{"form":form})