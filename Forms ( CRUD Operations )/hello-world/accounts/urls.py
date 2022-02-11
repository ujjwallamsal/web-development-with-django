
from django.urls import path
from .views import SignUpView ,password_change  , password_reset_form 
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path ('password_change/',password_change, name='password_change'),
    path ('password_reset/', password_reset_form, name='password_reset'),
    ]