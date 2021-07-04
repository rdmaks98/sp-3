from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

User_Type = [
    (0,'user'),
    (1,'broker'),
]

class UserForm(UserCreationForm):
    # first_name = forms.CharField(label='first name',
    #                        max_length=100,
    #                        widget=forms.TextInput(attrs={'class': 'form-control bg-gray'}))
    # last_name = forms.CharField(label='last name',
    #                        max_length=200,
    #                        widget=forms.TextInput(attrs={'class': 'form-control bg-gray'}))
    # email = forms.EmailField(max_length=100,required = True,help_text='Enter Email Address',
    #                     widget=forms.TextInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'Email'}))
    # mobile = forms.CharField(label='mobile',
    #                        max_length=240,
    #                        widget=forms.TextInput(attrs={'class': 'form-control bg-gray'}))
    # User_type = forms.ChoiceField(choices=User_Type, widget=forms.RadioSelect())
    # class Meta:
    #     model = User
    #     fields = ['first_name','last_name','username','email','mobile','User_type','password1' ,'password2']
    email = forms.EmailField(max_length=100,required = True,help_text='Enter Email Address',
    widget=forms.TextInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'Email'}),)

    first_name = forms.CharField(max_length=100,required = True,help_text='Enter First Name',
    widget=forms.TextInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'First Name'}),)

    last_name = forms.CharField(max_length=100,required = True,help_text='Enter Last Name',
    widget=forms.TextInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'Last Name'}),)

    username = forms.CharField(max_length=200,required = True,help_text='Enter Username',
    widget=forms.TextInput(attrs={'class': 'form-control bg-gray ', 'placeholder': 'Username'}),)

    password1 = forms.CharField(help_text='Enter Password',required = True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),)

    password2 = forms.CharField(required = True,help_text='Enter Password Again',
    widget=forms.PasswordInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'Password Again'}),)
    
    check = forms.BooleanField(required = True)

    class Meta:
        model = User
        fields = [
        'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'check',
        ]