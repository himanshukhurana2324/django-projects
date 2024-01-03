from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


            # CREATING THE REGISTER PAGE FOR THE USERS

def register(request):
     
    if request.method =='POST':
      name = request.POST['name']
      email = request.POST['email']
      username = request.POST['username']
      password = request.POST['password']
      confirm = request.POST['confirm']

      if password==confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email exists")
                return redirect('register')
            hjhjelse:
                user = User.objects.create_user(username= username, password= password, email= email,first_name=name)
                user.save();
               
                return redirect('login')
      else:
          messages.info(request, "password didnt matched")
          return redirect('register')


    else:
      return render(request,'register.html')
    # pass


                # CREATING A LOIN PAGE FOR THE EXISTING USERS
    

def login(request):
    
    if(request.method=='GET'):
        return render(request,'login.html') 
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)      

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')