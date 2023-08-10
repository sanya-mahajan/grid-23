from .views import *
from django.urls import path

urlpatterns = [
    path('create/',CreateTransaction.as_view(),name='create-transaction'),
]