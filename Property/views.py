# render and redirect request path url
from django.shortcuts import render,redirect,get_object_or_404

# return response that time using this
from django.http import HttpResponse

# user login and logout
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout

# after submit show success and error message
from django.contrib import messages,auth

from django.contrib.auth.models import User

# import models 
from .models import Agency,Profile,BrokerCategory,BrokerSubCategory

# Create your views here.

# index page 
def index(request):
    cat = BrokerCategory.objects.all()
    subcat = BrokerSubCategory.objects.all()
    # return render (request,'header.html',{'cat':cat})
    return render(request,"Property/index.html",{'cat':cat,'subcat':subcat})

# common user register here
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

# login user
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

# logout user
def logoutUser(request):
    django_logout(request)
    return redirect("login")

# user profile
def profile(request):
    # check user is login then display email 
    user = request.user

    # if profile is already submited then check in database
    data = Profile.objects.filter(u_id=user.id).count()
    if data > 0:
        data = Profile.objects.get(u_id=user.id)
        if data:
            return render(request,'user_page/profile.html',{'user':user,'data':data})
    # if this user data is not in the database then insert here
    elif request.method == 'POST':
        profile = Profile()
        # if profile.is_valid():
        profile.u_id = request.POST.get('u_id')
        profile.name=request.POST.get('name')
        profile.email=request.POST.get('email')
        profile.mobile=request.POST.get('mobile')
        profile.user_type=request.POST.get('user_type')
        profile.profile = request.FILES.get('profile')
        profile.dob = request.POST.get('dob')
        profile.details = request.POST.get('details')
        profile.save()
        messages.success(request,"your profile is done")
        return render(request,'user_page/profile.html',{'user':user})
    else:
        messages.error(request, 'Fill out all details')
        return render(request,'user_page/profile.html',{'user':user})

    return render(request,"user_page/profile.html",{'user':user})

def category(request,id):
    # show particular id wise property
    catdata = BrokerCategory.objects.get(id=id)

    # using this we can show selectbox catgory
    catall = BrokerCategory.objects.all()
    subcatall = BrokerSubCategory.objects.all()
    
    return render(request,"page/category.html",{'catdata':catdata,'catall':catall,'subcatall':subcatall})

def p_lists(request,id):
    subcat = get_object_or_404(BrokerSubCategory,id=id)
    return render(request,"page/p_lists.html",{'subcat':subcat})

def p_single(request):
    return render(request,"page/p_single.html")


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


# def categoryData(request):
    
