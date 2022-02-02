from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView 
from .models import Blog
from .forms import BlogForm
from django.urls import reverse_lazy 

def blogs(request):
    context = {
        'blogs': Blog.objects.all()  
    }
    return render(request, 'blogs/blogs.html', context)

def blog_detail(request, blog_id):
    context = {
        'blog': Blog.objects.get(id=blog_id)
    }
    return render(request, 'blogs/blog_detail.html', context)    




class BlogCreateView(CreateView): 
    model = Blog
    form_class = BlogForm
    template_name = 'blogs/blog_create.html'
    # fields = ['title','subtitle', 'author', 'body']  #or  fields = '__all__' 
   

class BlogUpdateView(UpdateView): 
    model = Blog
    #form_class = BlogForm
    template_name = 'blogs/blog_edit.html'
    fields = ['title','subtitle', 'body', 'author',] 


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blogs/blog_delete.html'
    success_url = reverse_lazy('blogs')       