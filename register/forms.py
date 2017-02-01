from django import forms
from .models import UserRegis

class UserRegisForm(forms.ModelForm) :
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta :
        model=UserRegis
        fields=[
            'first_name',
            'last_name',
            'email',
            'contact',
            'batch',
            'guardian_name',
            'guardian_email',
            'guardian_contact',
            'username',
            'password'
            
            ]
