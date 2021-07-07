from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

User_Type = [
    (0,'user'),
    (1,'broker'),
]

class UserForm(UserCreationForm):
   
    email = forms.EmailField(max_length=100,required = True,help_text='Enter Email Address',
    widget=forms.TextInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'Email'}),)

    name = forms.CharField(max_length=100,required = True,help_text='Enter Name',
    widget=forms.TextInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'First Name'}),)

    mobile = forms.CharField(max_length=100,required = True,help_text='Enter mobile',
    widget=forms.TextInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'Mobile number'}),)

    # User_type = forms.ChoiceField(choices=User_Type, widget=forms.RadioSelect()),

    username = forms.CharField(max_length=200,required = True,help_text='Enter Username',
    widget=forms.TextInput(attrs={'class': 'form-control bg-gray ', 'placeholder': 'Username'}),)

    password1 = forms.CharField(help_text='Enter Password',required = True,widget=forms.PasswordInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'Password'}),)

    password2 = forms.CharField(required = True,help_text='Enter Password Again',
    widget=forms.PasswordInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'Password Again'}),)
    
    check = forms.BooleanField(required = True)

    class Meta:
        model = User
        fields = [
        'username', 'email', 'name','mobile', 'password1', 'password2', 'check',
        ]

