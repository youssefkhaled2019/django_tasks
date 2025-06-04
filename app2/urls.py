from django.urls import path
from . import views

urlpatterns = [
    path('app2_index_1', views.index, name = 'app2'),
    path('app2_index_2', views.index2, name = "app2_index"),
    path('app2_index_3', views.index3, name = "app2_index_3"),
    path('upload2', views.fileupload, name = "app2_File_Uploads")
]