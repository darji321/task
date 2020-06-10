from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task


def home(request):
    return render(request, "home.html")

def login(request):
    if request.method== 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if Task.objects.filter(email=email,password=password).exists():
            profile=Task.objects.get(email=email)
            return render(request,'profile.html',{'profile':profile})   
        else:
            messages.info(request,'invalid credentials.....')
            return redirect('login')
            
    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        img=request.FILES['img']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if Task.objects.filter(email=email).exists():
                messages.info(request,'Email ID Taken.....')
                return redirect('register')
            else:   
                task = Task(img=img, password=password1, email=email,first_name=first_name,last_name=last_name)
                task.save();
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        
    else:
        return render(request,'register.html')
        
       
 