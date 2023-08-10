from .views import *
from django.urls import path

urlpatterns = [
    path('profile/',GetLoyaltyProfile.as_view(),name='loyalty-profile'),
    path('issue-points/',IssueLoyaltyPoints.as_view(),name='issue-points'),

]