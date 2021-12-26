from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class user_registerform(forms.Form):
    user_name = forms.CharField(max_length=40)
    email_user = forms.CharField(max_length=50)
    fname = forms.CharField(max_length=30)
    lname = forms.CharField(max_length=30)
    password_one = forms.CharField(max_length=20)
    password_two = forms.CharField(max_length=20)

    def clean_username(self):
        user = self.cleaned_data['user_name']

        if User.objects.filter(username=user).exists():
            raise forms.ValidationError("User  ")

        return user

    def clean_email(self):
        email = self.cleaned_data['email_user']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("email mojod ast")

        return email

    def clean_password_two(self):
        password1 = self.cleaned_data['password_one']
        password2 = self.cleaned_data['password_two']

        if password1 != password2:
            raise forms.ValidationError("password not match")

        elif len(password2) < 8 :
            raise forms.ValidationError("password ")
        return password1
