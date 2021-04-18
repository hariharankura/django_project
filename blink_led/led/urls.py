from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'control led'),
    url(r'^turnOn/', views.turnOn, name='turn on'),
    url(r'^turnOff/', views.turnOff, name='turn off'),
]