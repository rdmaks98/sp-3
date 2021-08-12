from django import forms

# agency model import here
from .models import Agency,UserProfile

# password change and resets
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy, gettext as _
from django.contrib.auth import password_validation

# change password 
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control mb-3'}))
    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control mb-3'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control '}))


# user profile 
class ProfileForm(forms.ModelForm):
    profile = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control bg-gray'}))

    name = forms.CharField(max_length=100,required = True,
    widget=forms.TextInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'enter ypor full name'}),)

    email = forms.CharField(max_length=100,required = True,
    widget=forms.TextInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'enter your mail id'}),)

    mobile = forms.IntegerField(required = True,
    widget=forms.TextInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'enter your mobile number'}),)

    user_type = forms.ChoiceField(required = True,
    widget=forms.TextInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'select user type'}),)

    details = forms.CharField(max_length=100,required = True,
    widget=forms.TextInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'enter your details'}),)

    class Meta:
        model = UserProfile
        fields = ["name","email","mobile","profile","user_type","details"]

# agency 
class AddAgency(forms.ModelForm):
    a_name = forms.CharField(max_length=100,required = True,
    widget=forms.TextInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'enter agency name'}),)

    a_address = forms.CharField(max_length=100,required = True,
    widget=forms.TextInput(attrs={'class': 'form-control bg-gray', 'placeholder': 'Agency address'}),)

    a_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control bg-gray'}))
    
    class Meta:
        model = Agency
        fields = ["a_name","a_image","a_address"]
        # widgets = {'u_id':forms.HiddenInput()}