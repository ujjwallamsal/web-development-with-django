from django.urls import path
from .views import homepageview , contactpageview , aboutpageview , blogpageview , postpageview

urlpatterns = [
    path('', homepageview.as_view(), name='home'),
    path('contact/', contactpageview.as_view(), name='contact'),
    path('blog/', blogpageview.as_view(), name='blog'),
    path('about/', aboutpageview.as_view(), name='about'),
     path('post/', postpageview.as_view(), name='post'),
]