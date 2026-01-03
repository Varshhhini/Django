from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_view')
def home(request):
    return HttpResponse('this is home')
        
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1==password2:
            user=User.objects.create_user(username=username,password=password1)
            return render(request,'login.html')
      
        return render(request,'register.html',{'info':'invalid password'})
    else:
        return render(request,'register.html')

def login_view(request):
    if request.method.lower()=='post':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'info':'Invalid credentials'})

    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')
    

# def login_required(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password = request.POST.get('password')
#         user=authenticate(username=username, password=password)
#         if user:
#             login(request,user)
#             return redirect('index')
#         else:
#             return render(request,'login.html',{'info': 'invalid credentials'})
#     else:
#        return render(request,'login.html')
    

