from . import views
from django.urls import path

app_name = 'bankapp'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('',views.home,name='home'),
    path('newpage',views.newpage,name='newpage'),
    path('form',views.form,name='form'),

]