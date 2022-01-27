from django.shortcuts import render
from django.views.generic import TemplateView

class homepageview(TemplateView):
    template_name = 'home.html'
class contactpageview(TemplateView):
    template_name = 'contact.html'
class aboutpageview(TemplateView):
    template_name = 'about.html'
class blogpageview(TemplateView):
    template_name = 'blog.html'
class postpageview(TemplateView):
    template_name = 'post.html'

# Create your views here.
