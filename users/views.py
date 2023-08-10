from django.shortcuts import render,redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate
from loyalties.models import *

class LoginView(APIView):
    def post(self,request):
        try:
            email=request.data['email']
            password=request.data['password']
        except:
            return Response({'status':'failed','message':'Please provide both email and password'},status=status.HTTP_400_BAD_REQUEST)
        if CustomUser.objects.filter(email=email).exists()==False:
            return Response({'status':'failed','message':'User does not exist'},status=status.HTTP_400_BAD_REQUEST)
        user=authenticate(email=email, password=password)
        
        token,_ = Token.objects.get_or_create(user=user)
        serializer=UserSerializer(user)

        #perday logic to do
        # if user.last_login.date()!=datetime.now().date():
        
        #give login points
        try:
            customer=Customer.objects.get(user=user)
        except:
            return Response({'status':'failed','message':'Invalid user type'},status=status.HTTP_400_BAD_REQUEST)
        try:
                profile=LoyaltyProfile.objects.get(customer=customer)
        except:
            return Response({'status':'failed','message':'No loyalty profile found'},status=status.HTTP_400_BAD_REQUEST)
        try:
            loyalty_type=Loyalty.objects.get(type="LOGIN")
        except:
            return Response({'status':'failed','message':'Invalid loyalty type'},status=status.HTTP_400_BAD_REQUEST)
        profile.current_points+=loyalty_type.points
        profile.maximum_points=max(profile.maximum_points,profile.current_points)
        profile.calculate_current_tier()
        profile.save()
        
        return Response({'status':'success','data':serializer.data,'token':str(token)},status=status.HTTP_200_OK)

    def LogoutView(self,request):
        request.user.auth_token.delete()
        return Response({'status':'success','message':'Logged out successfully'},status=status.HTTP_200_OK)

class CustomerDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user=request.user
        if user.user_type==1:
            customer=Customer.objects.get(user=user)
            serializer=CustomerSerializer(customer)
            return Response({'status':'success','data':serializer.data,'email':user.email},status=status.HTTP_200_OK)
        else:
            return Response({'status':'failed','message':'Invalid user type'},status=status.HTTP_400_BAD_REQUEST)