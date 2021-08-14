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
from .models import UserProfile,BrokerCategory,BrokerSubCategory,Agency

# import form
from .forms import AddAgency 

# Create your views here.
# index page 
def index(request):
    
    cat = BrokerCategory.objects.all()
    subcat = BrokerSubCategory.objects.all()
    agency = Agency.objects.all().order_by('-id')[0:4]
    company = Agency.objects.count()
    brokers = UserProfile.objects.filter(user_type='broker').count()
    data = UserProfile.objects.filter(userid_id=request.user.id).count()
    if data > 0:
        profile = UserProfile.objects.get(userid_id=request.user.id)
        return render(request,"Property/index.html",{'cat':cat,'subcat':subcat,'agency':agency,'profile':profile,'company':company,'brokers':brokers})
    return render(request,"Property/index.html",{'cat':cat,'subcat':subcat,'agency':agency,'company':company,'brokers':brokers})

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
            return redirect('profile')
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
    user = request.user
    # if this user data is not in the database then insert here
    if request.method == 'POST':
        add = UserProfile()
        # if profile.is_valid():
        add.userid_id = request.user.id
        add.name=request.POST.get('name')
        add.email=request.POST.get('email')
        add.mobile=request.POST.get('mobile')
        add.user_type=request.POST.get('user_type')
        add.profile = request.FILES.get('profile')
        add.dob = request.POST.get('dob')
        add.details = request.POST.get('details')
        add.save()
        messages.success(request,"your profile is done")
        return render(request,'user_page/profile.html',{'user':user})

    # user is already exist then display information
    elif UserProfile.objects.filter(userid_id=request.user.id).exists():
        profile = UserProfile.objects.get(userid_id=request.user.id)
        # print(profile)
        return render(request,'user_page/profile.html',{'user':user,'profile':profile})
    
    else:
        # messages.error(request, 'Fill out all details')
        return render(request,'user_page/profile.html',{'user':user})

    return redirect('user_page/profile.html',{'user':user,'data':data})

def category(request,id):
    # show particular id wise property
    catdata = BrokerCategory.objects.get(id=id)
    # using this we can show selectbox catgory
    catall = BrokerCategory.objects.all()
    subcatall = BrokerSubCategory.objects.all()
    
    return render(request,"page/category.html",{'catdata':catdata,'catall':catall,'subcatall':subcatall})

def p_lists(request,id):
    subcat = get_object_or_404(BrokerSubCategory,id=id)
    cat = BrokerCategory.objects.all()
    return render(request,"page/p_lists.html",{'subcat':subcat,'cat':cat})

def p_single(request):
    cat = BrokerCategory.objects.all()
    subcat = BrokerSubCategory.objects.all()
    return render(request,"page/p_single.html",{'cat':cat,'subcat':subcat})

def agency(request):
    # fetch cat,user and subcat data 
    cat = BrokerCategory.objects.all()
    subcat = BrokerSubCategory.objects.all()
    agency = Agency.objects.all().order_by('-id')[0:4]
    return render(request,"page/agency.html",{'cat':cat,'subcat':subcat,'agency':agency})

def addAgency(request):
    # fetched data from database
    cat = BrokerCategory.objects.all()
    subcat = BrokerSubCategory.objects.all()
    agency = Agency.objects.all().filter(u_id_id=request.user.id)
    # add agency data in the database with form
    if request.method == 'POST':
        form = AddAgency(request.POST,request.FILES)
        if form.is_valid():
            # save the form data to model
            user = request.user.id
            a_name = form.cleaned_data['a_name']
            a_image = form.cleaned_data['a_image']
            a_address = form.cleaned_data['a_address']
            agency = Agency(u_id_id=user, a_name=a_name, a_image=a_image, a_address=a_address)
            agency.save()
            messages.success(request, 'Your agency add successfully')
            return render(request,"page/Agency.html",{'cat':cat,'subcat':subcat,'form':form})
        else:
            messages.error(request, 'Fill all detail and enter valid value')
            return redirect('addAgency') 
    else:
        form = AddAgency()
        return render(request,"page/addAgency.html",{'cat':cat,'subcat':subcat,'form':form,'agency':agency})

    return render(request,"page/addAgency.html",{'cat':cat,'subcat':subcat,'agency':agency})

def broker(request):
    brokers = UserProfile.objects.filter(user_type="broker").all()
    return render(request,"page/broker.html",{'brokers':brokers})

def about(request):
    cat = BrokerCategory.objects.all()
    subcat = BrokerSubCategory.objects.all()
    return render(request,"page/about-us.html",{'cat':cat,'subcat':subcat})

def services(request):
    cat = BrokerCategory.objects.all()
    subcat = BrokerSubCategory.objects.all()
    return render(request,"page/services.html",{'cat':cat,'subcat':subcat})

def pricing(request):
    cat = BrokerCategory.objects.all()
    subcat = BrokerSubCategory.objects.all()
    return render(request,"page/pricing.html",{'cat':cat,'subcat':subcat})

def faq(request):
    cat = BrokerCategory.objects.all()
    subcat = BrokerSubCategory.objects.all()
    return render(request,"page/faq.html",{'cat':cat,'subcat':subcat})

def invoice(request):
    cat = BrokerCategory.objects.all()
    subcat = BrokerSubCategory.objects.all()
    return render(request,"page/invoice.html",{'cat':cat,'subcat':subcat})

def error404(request):
    cat = BrokerCategory.objects.all()
    subcat = BrokerSubCategory.objects.all()
    return render(request,"page/error404.html",{'cat':cat,'subcat':subcat})


# def categoryData(request):
    
