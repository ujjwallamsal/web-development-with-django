from django.shortcuts import render

from .models import post


def posts(request):
    context = {
        'posts': post.objects.all()  
    }
    return render(request, 'posts/posts.html', context)

