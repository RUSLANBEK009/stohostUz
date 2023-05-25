from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', SignupPage, name="signup"),
    path('login/', LoginPage, name="login"),
    path('auto/', AutoPage, name="auto"),
    path('logout/', LogoutPage, name="logout"),
]