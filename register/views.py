from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Person
# Create your views here.

# @login_required(login_url='login')

def SignupPage(request):
    if request.method=='POST':
        username=request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_obj=User.objects.filter(username=username).exists()
        if user_obj:
            messages.warning(request, 'This username already exists!')
        else:
            my_user = User.objects.create_user(username, email, password)
            my_user.save()
            person = Person.objects.create(user=my_user)
            person.save()
            return redirect('login')

    return render(request, template_name='registration/register.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('hosting_dashboard')
        else:
            messages.info(request, "Username or Password is incorrect!!!")
            # return HttpResponse("Username or Password is incorrect!!!")

    return render(request, template_name = 'registration/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def AutoPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj=User.objects.filter(username=username).exists()
        if user_obj:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or Password is incorrect!!!")
                return redirect('login')
        else:
            return render(request, template_name='registration/register.html', context={'username': username, 'password': password})
            

    return redirect('home')

