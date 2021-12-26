from . import views
from django.urls import path


app_name= 'acoounts'

urlpatterns=[
    path('register/',views.user_register,name='acoounts'),
]