# render and redirect request path url
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Max,Min
# return response that time using this
from django.http import HttpResponse

# user login and logout
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout

# after submit show success and error message
from django.contrib import messages,auth

from django.contrib.auth.models import User

# import models 
from .models import UserProfile,BrokerCategory,BrokerSubCategory,Agency,AddPropertyForm,Contact,Rating,Favourite

# import form
from .forms import AddAgency,Contactform,Rating_reviewform

# Create your views here.
# index page 
def index(request):
    
    cat = BrokerCategory.objects.all()
    subcat = BrokerSubCategory.objects.all()
    agency = Agency.objects.all().order_by('-id')[0:4]
    Propertyall = AddPropertyForm.objects.all().order_by('-id')[0:4]
    company = Agency.objects.count()
    p_c_f_sale = AddPropertyForm.objects.filter(propertyType="for sale").count()
    print(p_c_f_sale)
    p_c_f_rent = AddPropertyForm.objects.filter(propertyType="for rent").count()
    brokers = UserProfile.objects.filter(user_type='broker').count()
    data = UserProfile.objects.filter(userid_id=request.user.id).count()
    if data > 0:
        profile = UserProfile.objects.get(userid_id=request.user.id)
        return render(request,"Property/index.html",{'cat':cat,'subcat':subcat,'agency':agency,'profile':profile,'company':company,'brokers':brokers,'Propertyall':Propertyall,'p_c_f_sale':p_c_f_sale,'p_c_f_rent':p_c_f_rent})
    return render(request,"Property/index.html",{'cat':cat,'subcat':subcat,'agency':agency,'company':company,'brokers':brokers,'Propertyall':Propertyall,'p_c_f_sale':p_c_f_sale,'p_c_f_rent':p_c_f_rent})

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
        messages.warning(request, 'Please complete your profile')
        return render(request,'user_page/profile.html',{'user':user})

    return redirect('user_page/profile.html',{'user':user})

def category(request,id):
    # show particular id wise property
    catdata = BrokerCategory.objects.get(id=id)
    Property = AddPropertyForm.objects.all().filter(cate_id_id=id)
    catall = BrokerCategory.objects.all()
    subcatall = BrokerSubCategory.objects.all()
    return render(request,"page/category.html",{'catdata':catdata,'catall':catall,'subcatall':subcatall,'Property':Property})

def get_p_by_id(c_id,s_id):
    if c_id:
        return AddPropertyForm.objects.filter(cate_id_id = c_id)
    elif s_id:
        return AddPropertyForm.objects.filter(subcate_id_id=s_id)
    else:
        return AddPropertyForm.objects.all()

def p_lists(request,id):
    subcat = get_object_or_404(BrokerSubCategory,id=id)
    cat = BrokerCategory.objects.all()
    property = AddPropertyForm.objects.filter(subcate_id_id=id).all()
    return render(request,"page/p_lists.html",{'cat':cat,'subcat':subcat,'property':property})

def p_single(request,id):
    property_single = AddPropertyForm.objects.get(id=id)
    rating = Rating.objects.all().order_by('Rid')[0:4]
    if request.method == "POST":
        add = Rating()
        add.uid_id = request.user.id
        add.pid_id = property_single.id
        add.name=request.POST.get('name')
        add.rate=request.POST.get('rate')
        add.review=request.POST.get('review')
        add.save()
        messages.success(request,"your Rating and review is submitted")
        return redirect("index")
    else:
        messages.error(request,"enter valid details")
        return render(request,"page/p_single.html",{'property_single':property_single,'rating':rating})
    
    return render(request,"page/p_single.html",{'property_single':property_single,'rating':rating})

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
    
def Update(request):
    user = request.user.id
    agency = Agency.objects.all().filter(u_id_id=request.user.id)
    if request.method == "POST":
        id = request.POST.get('id')
        a_name = request.POST.get('a_name')
        a_address = request.POST.get('a_address')
        a_image = request.FILES.get('a_image')
        print(a_image)
        updatedata = Agency.objects.get(id=id)
        updatedata.id = id
        updatedata.a_name = a_name
        updatedata.a_address = a_address
        updatedata.a_image = a_image
        updatedata.save()
        data = {'id':updatedata.id,'a_name':updatedata.a_name,'a_address':updatedata.a_address,'a_image':updatedata.a_image}

        agency = {
            'data': data
        }
        messages.success(request, 'Your agency update successfully')
        return render(request,"page/addAgency.html",{'agency':agency})
        # form = AddAgency(request.POST)
        # # print(form)
        # if form.is_valid():
        #     print("if")
        #     a_id = request.GET.get('a_id', None)
        #     a_name = request.GET.get('a_name', None)
        #     a_address = request.GET.get('a_address', None)
        #     a_image = request.GET.get('a_image', None)
        #     # agency = Agency(u_id_id=user,a_id=a_id, a_name=a_name, a_image=a_image, a_address=a_address)
        #     # print(agency)
        #     agency.save()
        #     messages.success(request, 'Your agency add successfully')
        #     return render(request,"page/Agency.html",{'form':form})
        # else:
        #     messages.error(request, 'Fill all detail and enter valid value')
        #     return redirect('addAgency') 
    else:
        form = AddAgency()
    return render(request,"page/addAgency.html",{'form':form,'agency':agency})
        
def addProperty(request): 
    cate = BrokerCategory.objects.all()
    subcate = BrokerSubCategory.objects.all()
    agency = Agency.objects.all().filter(u_id_id=request.user.id)
    if request.method == 'POST':
        addProperty = AddPropertyForm()
        addProperty.user_id_id = request.user.id
        addProperty.propertyTitle = request.POST['propertyTitle']
        addProperty.propertyType = request.POST['propertyType']#DropDown
        addProperty.price = request.POST['price']
        addProperty.propertyDescription = request.POST['propertyDescription']
        addProperty.address = request.POST['address']
        addProperty.city = request.POST['city']
        addProperty.zip = request.POST['zip']
        addProperty.areasize = request.POST['areasize']
        addProperty.builtyear = request.POST['builtyear']
        addProperty.cate_id_id = request.POST['cate_id_id']
        addProperty.subcate_id_id = request.POST['subcate_id_id']
        addProperty.aid_id = request.POST['aid_id']
        addProperty.propertyimage = request.FILES['propertyimage']
        addProperty.propertybrochure = request.FILES['propertybrochure']
        addProperty.propertyplanimage = request.FILES['propertyplanimage']
        addProperty.propertyvideo = request.FILES['propertyvideo']
        print(addProperty.propertyimage)
        addProperty.save()
        messages.success(request,"your property added successfully")
        return redirect("index")
    return render(request,'page/addproperty.html',{'cate':cate,'agency':agency,'subcate':subcate})

def features(request):
    propertyData = AddPropertyForm.objects.all()
    return render(request,'layout/features.html',{'propertyData':propertyData})

def broker(request):
    brokers = UserProfile.objects.filter(user_type="broker").all()
    return render(request,"page/broker.html",{'brokers':brokers})

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

def contact(request):  
    if request.method == "POST":
        form = Contactform(request.POST)
        user = request.user.id
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contactadd = Contact(uid_id=user,name=name,email=email,message=message)
            contactadd.save()
            messages.success(request,"your message send succesfully")
            return redirect("index")
        else:
            messages.error(request,"enter valid details")
    else:
        form = Contactform()
        return render(request,"page/contact.html",{'form':form})
    
    return render(request,"page/contact.html")

def favourite(request):
    user = request.user.id
    
    if request.method == "POST":
        product_id = request.POST.get('pid_id')
        if Favourite.objects.filter(pid_id=product_id,uid_id=user).exists():
            messages.error(request,"you have already add in favourite")
            return render(request,"page/favourite_property.html")
        else:
            Favourite(pid_id=product_id,uid_id=user).save()
            return render(request,"page/favourite_property.html")
    else:
        fp = Favourite.objects.filter(uid_id=user).all()
        # filter(uid_id=user).all()
        return render(request,"page/favourite_property.html",{"fp":fp})
    return render(request,"page/favourite_property.html")

# def categoryData(request):    