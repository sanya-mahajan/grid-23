from .views import *
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),   
    path('profile/', CustomerDetail.as_view(), name='customer-detail'),
    
    ]