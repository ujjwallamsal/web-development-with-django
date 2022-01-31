from django.shortcuts import render

from .models import blog

def blogs(request):
    context = {
        'blogs': blog.objects.all()  }
    return render(request, 'blogs/blogs.html', context)

def blog_detail(request, blog_id):
    context = {
        'blog': blog.objects.get(id=blog_id)
    }
    return render(request, 'blogs/blog_detail.html', context)