from django.shortcuts import render
import string
import random
# Create your views here.
from django.shortcuts import render, redirect
from .forms import ImagesForm,ArtcalsForm
from .models import Post,Data
import os
import shutil
from django.conf import settings
# Create your views here.
# def index(request):
#     images = Image.objects.all()
#     images
#     context = {'images': images}
#     return render(request, "uplode_1.html", context)

KEY_LEN = 16

def base_str():
    return (string.ascii_letters + string.digits)   
def key_gen():
    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
    return ("".join(keylist))

# def index(request):
#     data={}
#     temp=[]
#     for i in  Post.objects.all():
#         for j in Data.objects.filter(artcal=i):
#             temp.append(j)
#         data[i]=temp
#         temp=[]
#     context = {'data': data}
#     return render(request, "uplode_11523.html", context)



def index(request):
 
    data=Post.objects.prefetch_related("data").all()
    context = {'data': data}
    return render(request, "app5_index.html", context)


def index1(request):
 
    data=Post.objects.prefetch_related("data").all()
    form2 = ArtcalsForm()
    form = ImagesForm()

    if request.method == 'POST':
        form2 = ArtcalsForm(request.POST)
        form = ImagesForm(request.POST, request.FILES)
        images = request.FILES.getlist('name_file')
        print("test0")

        if form.is_valid() or form2.is_valid():
            print("test1")
            title = form2.data['title']
            folder_name=key_gen()
            artcals=Post.objects.create(title=title,folder_name=folder_name)
            
            for image in images:
                print("image_name",image.name,image.name.split(".")[-1])
                if image.name.split(".")[-1] in ["mp4"]:  # if "mp4" in image.name:
                   
                    # print("v") albumname
                   image_ins = Data.objects.create(albumname =folder_name ,name_file = image,artcal=artcals,type=1)
                elif image.name.split(".")[-1]  in ["jpg","png"] :         #else:
                    # print("i")
                   image_ins = Data.objects.create(albumname =folder_name,name_file = image,artcal=artcals,type=0)    
                # image_ins.save() 
            return redirect('app5_index1')


    context = {'data': data,'form': form,'form2': form2}
    return render(request, "app5_index1.html", context)


def fileupload(request):
    form2 = ArtcalsForm()
    form = ImagesForm()

    if request.method == 'POST':
        form2 = ArtcalsForm(request.POST)
        form = ImagesForm(request.POST, request.FILES)
        images = request.FILES.getlist('name_file')
        print("test0")

        if form.is_valid() or form2.is_valid():
            print("test1")
            title = form2.data['title']
            folder_name=key_gen()
            artcals=Post.objects.create(title=title,folder_name=folder_name)
            for image in images:
                if "mp4" in image.name:
                    # print("v") albumname
                   image_ins = Data.objects.create(albumname =folder_name ,name_file = image,artcal=artcals,type=1)
                else:
                    # print("i")
                   image_ins = Data.objects.create(albumname =folder_name,name_file = image,artcal=artcals,type=0)    
                # image_ins.save() 
            return redirect('app5')
    context = {'form': form,'form2': form2}
    return render(request, "app5_uploade.html", context)

def update(request,id):
    post=Post.objects.get(id=id)
    form2 = ArtcalsForm(instance=post)
    form = ImagesForm()

    if request.method == 'POST':
        post=Post.objects.get(id=id)
        folder_name_old=post.folder_name
        form2 = ArtcalsForm(request.POST,instance=post)
        form = ImagesForm(request.POST, request.FILES)
        images = request.FILES.getlist('name_file')
        if form.is_valid() or form2.is_valid():
            title = form2.data['title']
            folder_name=key_gen()
            # artcals=Post.objects.create(title=title,folder_name=folder_name)
            post.folder_name=folder_name
            post.save()
            # print( post.data_set.all()  )#aiter_set.all()
            Data.objects.filter(artcal=post).delete()
            for image in images:
                if "mp4" in image.name:
                    # print("v") albumname
                   image_ins = Data.objects.create(albumname =folder_name ,name_file = image,artcal=post,type=1)
                else:
                    # print("i")
                   image_ins = Data.objects.create(albumname =folder_name,name_file = image,artcal=post,type=0)    

            folder_path = os.path.join(settings.MEDIA_ROOT,'uploads', folder_name_old)
            print(folder_path)
            if os.path.isdir(folder_path):
                shutil.rmtree(folder_path)
        
                return redirect('app5_index1')
            else:
                print("error")
                return redirect('app5_index1')       
                # image_ins.save() 
            # return redirect('app5')
    context = {'form': form,'form2': form2}
    return render(request, "app5_uploade.html", context)


def delete(request,id):
    data=Post.objects.get(id=id)
    folder_path = os.path.join(settings.MEDIA_ROOT,'uploads', data.folder_name)
    print(folder_path)
    if os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
        data.delete()
        return redirect('app5_index1')
    else:
        print("error")
        data.delete()
        return redirect('app5_index1')
        # Proceed to remove the folder
#   H:\2025\django-project\django_tasks\media\uploads\Iw4gna8LBuMvQFnG


# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
#  '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__',
#  '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
#  '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
#  '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index',
#  'insert', 'pop', 'remove', 'reverse', 'sort']