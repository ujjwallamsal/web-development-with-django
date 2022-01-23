from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

# def homePageView(request):
#     return HttpResponse('Hello, World!')

# def aboutpage(request):
#     return HttpResponse('this is come from aboutpage')

# def contactpage(request):
#     return HttpResponse('this is come from contactpage')

# def projectpage(request):
#     return HttpResponse('this is coming from projectpage')

from django.views.generic import TemplateView 

class basePageView(TemplateView):
    template_name = 'base.html'  
class HomePageView(TemplateView):
    template_name = 'home.html'  
class aboutPageView(TemplateView):
    template_name = 'about.html'
class postPageView(TemplateView):
    template_name = 'post.html'
class blogPageView(TemplateView):
    template_name = 'blog.html'
class contactPageView(TemplateView):
    template_name = 'contact.html'
