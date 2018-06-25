from django.urls import path
from . import views

urlpatterns = [
                path('', views.home,name='home'),
                path('contact/', views.contact,name='contact'),
                path('profile/', views.profile,name='profile'),
                path('login/', views.login,name='login'),
                path('signup/', views.signup,name='signup'),
                path('mklogin/',views.mklogin,name='mklogin'),
                path('mksignup/',views.mksignup,name='mksignup'),


]