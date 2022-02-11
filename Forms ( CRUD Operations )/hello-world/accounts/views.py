from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def password_change(request):
    return render(request, 'registration/password_change_form.html')


def password_reset_form(request):
    return render(request, 'registration/password_reset_form.html')
