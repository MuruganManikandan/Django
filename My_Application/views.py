from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import Datas
from .form import CreateUserForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request,"home.html")

@login_required(login_url='Login')
def Project(request):
    return render(request,"Project.html")

def CGVML(request):
    return render(request,"CGVML.html")

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        mail=request.POST['mail']
        number=request.POST['number']
        msg=request.POST['msg']


        obj=Datas()
        obj.Name=name
        obj.mail=mail
        obj.number=number
        obj.msg=msg
        obj.save()
        messages.success(request,'Your message has been sended...')
    return render(request,"contact.html")

#def loginpage(request):
    #return render(request,"loginpage.html")

def signuppage(request):
    if request.method=='POST':
        name=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        
        if password1==password2:
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff=True
            user.save()
            messages.success(request,'Your accound has been created! Now you can able to login...')
            return redirect('Login')
        else:
            messages.warning(request,'Password Missmatching......')
            return redirect('Signuppage')
    else:
        form=CreateUserForm()
        return render(request,"signuppage.html",{'form':form})


@login_required(login_url='Login')
def exampledata(request):
    if request.method=='POST':
        name=request.POST['name']
        mail=request.POST['mail']
        number=request.POST['number']
        msg=request.POST['msg']


        obj=Datas()
        obj.Name=name
        obj.mail=mail
        obj.number=number
        obj.msg=msg
        obj.save()
    return render(request,"exampledata.html")


