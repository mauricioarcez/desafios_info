from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from django.urls import reverse_lazy
from .forms import RegisterUserForm

# Create your views here.
class RegisterUser(CreateView):
    model = User
    template_name = 'user/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')