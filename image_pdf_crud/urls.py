from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [

    path("", views.index ,name="home"),
    path("add",views.add,name="add_row"),
    path("show_item/<int:id>",views.show_item,name="show_item"),
    path("delete/<int:id>",views.delete,name="delete_row"),
    path("download/<int:id>/",views.download,name="download_pdf"),
    path("search",views.search,name="search")

    # path("search<str:name>/",views.search,name="search")

]