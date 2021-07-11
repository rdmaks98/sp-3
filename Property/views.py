from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib import messages
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
            return render(request,'user_page/login.html')
    return render(request,'user_page/login.html')

def logoutUser(request):
    django_logout(request)
    return redirect("login")

def register(request):
    # sample code
    # if request.method == 'POST':
    #     form  = UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         user = form.cleaned_data.get('username')
    #         messages.success(request, 'Account was created for ' + user)
    #         return redirect('login')
    # else:
    #     print('Form is not valid')
    #     messages.error(request, 'Error Processing Your Request')
    #     context = {'form': form}
    #     return render(request, 'user_page/register.html', context)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("registration successfully")
            return redirect('login')
    else:
        form =UserCreationForm()
     
    return render(request,"user_page/register.html",{'form':form})

# def categoryData(request):
    
