from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# ______________________________________________________________________________________________________________________

def user_registration (request):
   
   if request.user.is_authenticated:
      return redirect('/pages/home')
   if request.method == 'POST':
      username = request.POST.get('name')
      email = request.POST.get('email')
      password = request.POST.get('password')
      
      user_check =  User.objects.filter(username=username)
      if user_check.exists():
         messages.info(request,'User with this username already exists')
         return render(request, 'register.html')
      user = User.objects.create_user(username=username, email=email, password=password)
      user.save() 
      
      messages.success (request, 'User registed Sucessfully')
   return render(request, 'register.html')

# # ______________________________________________________________________________________________________________________

def user_login(request):
   if request.user.is_authenticated:
      return redirect('/pages/home')
   if(request.method == 'POST'):
      username = request.POST.get('name')
      password = request.POST.get('password')
      user_check = User.objects.filter(username=username)
      if not user_check.exists()  :
         messages.info(request, 'User doesnot exist')
         return render(request, 'login.html')
      
      user = authenticate(request,  username=username, password=password)
      if user is  None:
         messages.info(request, 'Password is wronge')
         return render(request, 'login.html')
      
      login(request, user)
      messages.success(request, 'Login Successfull')
      return redirect('/pages/home')
   
   return render(request, 'login.html')
   
   
# ______________________________________________________________________________________________________________________

def user_logout(request):
   logout(request)
   messages.info(request, 'logout successfull')
   return redirect('/pages/home')