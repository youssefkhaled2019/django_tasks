from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ImagesForm,ArtcalsForm
from app2.models import Image,Artcals

# Create your views here.
# def index(request):
#     images = Image.objects.all()
#     images
#     context = {'images': images}
#     return render(request, "uplode_1.html", context)


def index(request):
    data={}
    temp=[]
    for i in  Artcals.objects.all():
        for j in Image.objects.filter(artcal=i):
            temp.append(j)
        data[i]=temp
        temp=[]
    context = {'data': data}
    return render(request, "app2_index_1.html", context)



def index2(request):
    data={}
    temp=[]

    form2 = ArtcalsForm()
    form = ImagesForm()

    if request.method == 'POST':
        form2 = ArtcalsForm(request.POST)
        form = ImagesForm(request.POST, request.FILES)
        images = request.FILES.getlist('pic')
        print("test0")

        if form.is_valid() or form2.is_valid():
            print("test1")
            title = form2.data['title']
            artcals=Artcals.objects.create(title=title)
            for image in images:

                image_ins = Image.objects.create(pic = image,artcal=artcals)
                image_ins.save()
            return redirect('app2_index')
        
    for i in  Artcals.objects.all():
        for j in Image.objects.filter(artcal=i):
            temp.append(j)
        data[i]=temp
        temp=[]
    context = {'data': data,'form': form,'form2': form2}
    return render(request, "app2_index_2.html", context)



def index3(request):


    form2 = ArtcalsForm()
    form = ImagesForm()
    data=Artcals.objects.prefetch_related("images").all()
    # print(data[0].artcal.all)
    if request.method == 'POST':
        
        form2 = ArtcalsForm(request.POST)
        form = ImagesForm(request.POST, request.FILES)
        images = request.FILES.getlist('pic')
        # print("test0")

        if form.is_valid() or form2.is_valid():
            # print("test1")
            title = form2.data['title']
            artcals=Artcals.objects.create(title=title)
            for image in images:

                image_ins = Image.objects.create(pic = image,artcal=artcals)
                image_ins.save()
            return redirect('app2_index_3')
        


   




    context = {'data': data,'form': form,'form2': form2}
    return render(request, "app2_index_3.html", context)


def fileupload(request):
    form2 = ArtcalsForm()
    form = ImagesForm()

    if request.method == 'POST':
        form2 = ArtcalsForm(request.POST)
        form = ImagesForm(request.POST, request.FILES)
        images = request.FILES.getlist('pic')
        print("test0")

        if form.is_valid() or form2.is_valid():
            print("test1")
            title = form2.data['title']
            artcals=Artcals.objects.create(title=title)
            for image in images:

                image_ins = Image.objects.create(pic = image,artcal=artcals)
                image_ins.save()
            return redirect('app2')
    context = {'form': form,'form2': form2}
    return render(request, "app2_uplode.html", context)