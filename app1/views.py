from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ImagesForm
from .models import Image

# Create your views here.
def index(request):
    images = Image.objects.all()

    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        images = request.FILES.getlist('pic')
        for image in images:
            image_ins = Image(pic = image)
            image_ins.save()
        return redirect('index')
    if request.method == 'GET':
        form= ImagesForm()



    
    context = {'images': images,'form': form}
    # return render(request, "uplode_1.html", context)
    return render(request, "index1.html", context)
    
