from django.urls import path
from .views import *


urlpatterns = [
    path('',IndexView.as_view(), name="home"),
    path('about/', about, name="about"),
    path('abuse/', abuse, name="abuse"),
    path('terms/', terms, name="terms"),
    path('contact/', contact, name="contact"),
    #SERVICES
    path('vps/', vpsserver, name="vps_server"),
    path('hosting/', hosting, name="hosting"),
    path('domains/', domains, name="domains"),
    
]