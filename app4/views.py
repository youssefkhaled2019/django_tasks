from django.shortcuts import render
import string
import random
# Create your views here.
from django.shortcuts import render, redirect
from .forms import ImagesForm,ArtcalsForm
from .models import Post,Data

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
    return render(request, "app4_index.html", context)


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
            artcals=Post.objects.create(title=title)
            name_folder=key_gen()
            for image in images:
                print("image_name",image.name,image.name.split(".")[-1])
                if image.name.split(".")[-1] in ["mp4"]:  # if "mp4" in image.name:
                   
                    # print("v") albumname
                   image_ins = Data.objects.create(albumname =name_folder ,name_file = image,artcal=artcals,type=1)
                elif image.name.split(".")[-1]  in ["jpg","png"] :         #else:
                    # print("i")
                   image_ins = Data.objects.create(albumname =name_folder,name_file = image,artcal=artcals,type=0)    
                # image_ins.save() 
            return redirect('app4_index1')


    context = {'data': data,'form': form,'form2': form2}
    return render(request, "app4_index1.html", context)


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
            artcals=Post.objects.create(title=title)
            name_folder=key_gen()
            for image in images:
                if "mp4" in image.name:
                    # print("v") albumname
                   image_ins = Data.objects.create(albumname =name_folder ,name_file = image,artcal=artcals,type=1)
                else:
                    # print("i")
                   image_ins = Data.objects.create(albumname =name_folder,name_file = image,artcal=artcals,type=0)    
                # image_ins.save() 
            return redirect('app4')
    context = {'form': form,'form2': form2}
    return render(request, "app4_uploade.html", context)



# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
#  '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__',
#  '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
#  '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
#  '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index',
#  'insert', 'pop', 'remove', 'reverse', 'sort']