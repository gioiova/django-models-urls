from django.views.generic import CreateView
from .form import CustomUserCreationForm
class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url  = '/'