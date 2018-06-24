from django.urls import path
from . import views

urlpatterns = [
                path('', views.home),
                path('mayanksharma/',views.client),

]