from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import models, forms
from django.views import generic


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:home')


class RegistrationView(CreateView):
    form_class = forms.CustomRegisterForm
    # form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'users/register.html'


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('users:post')


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'users/homepage.html'

    def get_queryset(self):
        return User.objects.all()


class RegisterSuccesViews(generic.ListView):
    template_name = 'users/homepage.html'
    queryset = models.RegisterSucces.objects.all()

    def get_queryset(self):
        return models.RegisterSucces.objects.all()
