from django.urls import path
from .views import homepageview , contactpageview , aboutpageview , blogpageview 

urlpatterns = [
    path('', homepageview.as_view(), name='home'),
    path('contact/', contactpageview.as_view(), name='contact'),
    path('blog/', blogpageview.as_view(), name='blog'),
    path('about/', aboutpageview.as_view(), name='about'),
    
]