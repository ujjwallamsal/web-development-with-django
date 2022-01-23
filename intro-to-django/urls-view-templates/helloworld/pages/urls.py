from django.urls import path
from .views import *

urlpatterns = [
        path('', basePageView.as_view(), name='base'),
        path('home/', HomePageView.as_view(), name='home'),
        path('blog/', blogPageView.as_view(), name='blog'),
        path('about/', aboutPageView.as_view(), name='about'),
        path('post/', postPageView.as_view() , name='post'),
        path('contact/', contactPageView.as_view() , name='contact')
]
