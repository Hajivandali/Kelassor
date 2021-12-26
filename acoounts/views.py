from django.shortcuts import render,redirect
from .forms import user_registerform
# Create your views here.
from django.contrib.auth.models import User

def user_register(request):
    if request.method == 'POST':
        form = user_registerform(request.POST)
        if form.is_valid():    #etebar sanji clean method az clean dec migirim
            data = form.cleaned_data
            User.objects.create_user(username=data['user_name'], email=data['email_user'], first_name=data['fname'], last_name=data['lname'],
                                     password=data['password_two'])
            return redirect('home:home')
    else:
        form = user_registerform()
    contex = {'form': form}

    return render(request, 'login.html', contex)