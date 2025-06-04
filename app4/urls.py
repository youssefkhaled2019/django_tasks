from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'app4'),
    path('app4_index1', views.index1, name = 'app4_index1'),
    path('upload', views.fileupload, name = "app4_File_Uploads")
]