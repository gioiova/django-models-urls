from django.http import HttpResponse
from django.views.generic import CreateView
from .form import CustomUserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from .models import CustomUser
from django.contrib import messages

class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url  = reverse_lazy('user:login')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False 
        user.save()
        
        user_token = default_token_generator.make_token(user)
        activation_link = self.request.build_absolute_uri(reverse_lazy('user:activate', kwargs={'user_pk': user.pk, 'token': user_token}))
        
        send_mail('Activate your account', f'Hi {user.username},\n\nClick the link to activate your account: {activation_link}', '', [user.email])        

        messages.success(self.request, 'Account created successfully! Please check your email to activate your account.')   
        
        return redirect('user:login')

def activate_user(request,user_pk,token):
    user = CustomUser.objects.get(pk=user_pk)
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        
        messages.success(request, 'Your account has been activated successfully! You can now log in.')
        return redirect('user:login')
    
    messages.warning(request, 'Activation link is invalid or has expired.')
    return redirect('/')

class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = '/'

