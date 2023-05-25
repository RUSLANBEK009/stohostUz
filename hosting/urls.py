from django.urls import path
from .views import *


urlpatterns = [
    path('hosting/', Dashboard, name="hosting_dashboard"),
    path('finances/deposit/', Deposit, name="deposit"),
    path('finances/history/', BalanceHistory, name="balance_history"),
    path('hosting/<str:site>', Site)
]