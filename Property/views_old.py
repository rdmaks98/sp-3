from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"Property/index.html")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return render(request,'user_page/login.html')
    return render(request,'user_page/login.html')

def logoutUser(request):
    django_logout(request)
    return redirect("login")

def category(request):
    return render(request,"page/category.html")

def p_single(request):
    return render(request,"page/p_single.html")

def p_lists(request):
    return render(request,"page/p_lists.html")

def agency(request):
    return render(request,"page/agency.html")
     
def broker(request):
    return render(request,"page/broker.html")

def about(request):
    return render(request,"page/about-us.html")

def services(request):
    return render(request,"page/services.html")

def pricing(request):
    return render(request,"page/pricing.html")

def faq(request):
    return render(request,"page/faq.html")

def invoice(request):
    return render(request,"page/invoice.html")

def error404(request):
    return render(request,"page/error404.html")

def profile(request):
    return render(request,"user_page/profile.html")

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("registration successfully")
            return redirect('login')
    else:
        form =UserCreationForm()
     
    return render(request,"user_page/register.html",{'form':form})


