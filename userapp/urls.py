from django.urls import path
from .views import register, email_verification, login, password_reset


app_name = 'userapp'

urlpatterns = [
    path('register/', register, name='register'),
    path('email_verification/', email_verification, name='email_verification'),
    path('login/', login, name='login'),
    path('password_reset/', password_reset, name='password_reset'),

]

