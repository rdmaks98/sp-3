from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib import messages,auth
from .models import Agency

# new 
# from django.contrib import messages, auth
from django.contrib.auth.models import User
from Property.models import BrokerCategory,BrokerSubCategory

# Create your views here.
def index(request):
    cat = BrokerCategory.objects.all()
    subcat = BrokerSubCategory.objects.all()
    # return render (request,'header.html',{'cat':cat})
    return render(request,"Property/index.html",{'cat':cat,'subcat':subcat})

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request,'user_page/login.html')
    else:
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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        image = request.FILES['image']
        data = Agency(name=name,email=email,mobile=mobile,image=image)
        data.save()
        
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

# website user
def register(request):
    if request.method == 'POST':
        #Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            #  Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The email already exists')
                    return redirect('register')
                else:
                    # Everything passed
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after register
                    user.save()
                    messages.success(request, 'You are now registered and can Log In')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'user_page/register.html')

# def categoryData(request):
    
