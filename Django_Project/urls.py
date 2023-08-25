"""
URL configuration for Django_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from My_Application import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.home),
    path('home', views.home,name="Home"),
    path('Project', views.Project,name="Project"),
    path('CGVML', views.CGVML,name="CGVML"),
    path('contact', views.contact,name="contact"),
   # path('loginpage', views.loginpage,name="Login"),
    path("loginpage/",auth_views.LoginView.as_view(template_name='loginpage.html'),name="Login"),
    path("logout/",auth_views.LogoutView.as_view(template_name='home.html'),name="Logout"),
    path('signuppage', views.signuppage,name="Signuppage"),
    path('exampledata', views.exampledata,name="exampledata"),
]
