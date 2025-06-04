from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'app3'),
    path('index1', views.index1, name = 'app3_index1'),
    path('uplode', views.fileupload, name = "app3_File_Uploads")
]