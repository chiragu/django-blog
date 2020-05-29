from django.shortcuts import render

# import generic user creation form
from django.contrib.auth.forms import UserCreationForm

# reverse lazy for redirect to login page after adding user
from django.urls import reverse_lazy

# create view
from django.views.generic import CreateView

# Create your views here.

class SignUpView(CreateView):
    
    # form class
    form_class = UserCreationForm

    # on success redirect to login url
    success_url = reverse_lazy('login')

    # template for class
    template_name = 'accounts/signup.html'


