from django.views.generic import CreateView
from .form import CustomUserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url  = reverse_lazy('user:login')

class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = '/'

