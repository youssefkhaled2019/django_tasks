from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.home,name="home"),
    path('login/', LoginView.as_view(template_name="user/login.html"),name="login"),
    path('logout', LogoutView.as_view(template_name="user/logout.html"),name="logout"),
    path('about', views.about,name="about"),
    # path('login_', views.login,name="login_"),
    path('register', views.register,name="register"),
    path('profile', views.profile,name="profile"),

]