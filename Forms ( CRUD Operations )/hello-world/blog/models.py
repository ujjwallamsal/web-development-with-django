
from django.db import models
from django.urls import reverse 
from config import settings
User = settings.AUTH_USER_MODEL
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='User') 
    body = models.TextField()
    subtitle = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse('blog_detail', args=[str(self.id)])