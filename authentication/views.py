from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as a,login as l,logout as lo
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def loginView(request):
    if(not request.user.is_authenticated):
        return render(request,'pages/login.html')
    else:
        return redirect('/')
    

def registerView(request):
    if(not request.user.is_authenticated):
        return render(request,'pages/register.html')
    else:
        return redirect('/')


def authenticate(request):
    if request.method=='POST':
        user_name=request.POST['username']
        password=request.POST['password']

        user=a(request,username=user_name,password=password)
        errors=None

        if user is not None:
            l(request,user)
            return redirect('/')
        else:
            errors='Invalid credentials'
            data={
                'username':user_name,
                'password':password
            }
            return render(request,'pages/login.html',{'data':data,'errors':errors})
    

def register(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        user_name=request.POST['uname']
        password=request.POST['password']
        repassword=request.POST['repassword']
        errors=None

        if not first_name or not last_name or not email or not user_name or not password:
            errors='Field must not be empty'
        elif password!=repassword:
            errors='Password not matched'
        elif User.objects.filter(email=email).exists():
            errors='Email already in use'
        elif User.objects.filter(username=user_name).exists():
            errors='Username already taken'
        
        if not errors:
            user=User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            return redirect('loginView')
        else:
            data={
                'fname':first_name,
                'lname':last_name,
                'email':email,
                'username':user_name,
            }
            return render(request,'pages/register.html',{'data':data,'errors':errors})
    
def logout(request):
    lo(request)
    return redirect('/')