from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'app5'),
    path('app5_index1', views.index1, name = 'app5_index1'),
    path('upload', views.fileupload, name = "app5_File_Uploads"),
    path('delete/<int:id>/', views.delete, name = "app5_delete"),
    path('update/<int:id>/', views.update, name = "app5_update"),
]