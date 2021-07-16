from django import forms

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
