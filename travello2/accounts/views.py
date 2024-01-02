from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def register(request):

    if request.method =='POST':
      name = request.POST['name']
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      confirm = request.POST['confirm']

      if password==confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username= username, password= password, email= email,first_name=name)
                user.save();
               
                return redirect('/')
      else:
          messages.info(request, "password didnt matched")
          return redirect('register')


    else:
      return render(request,'register.html')
    # pass