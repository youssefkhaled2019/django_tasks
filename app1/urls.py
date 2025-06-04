from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'app1'),
    path('upload', views.fileupload, name = "app1_File_Uploads")
]