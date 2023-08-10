from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class GetLoyaltyProfile(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user=request.user
        if user.user_type!=1:
            return Response({'status':'failed','message':'Invalid user type'},status=status.HTTP_400_BAD_REQUEST)
        
        else:
            customer=Customer.objects.get(user=user)
            profile=LoyaltyProfile.objects.get(customer=customer)
            serializer=LoyaltyProfileSerializer(profile)
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
    
class GetLoyaltyTypes(APIView):
    def get(self,request):
        loyalty_types=Loyalty.objects.all()
        serializer=LoyaltySerializer(loyalty_types,many=True)


        return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
    

class IssueLoyaltyPoints(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        try:
            loyalty_type=request.data['loyalty_type']
        except:
            return Response({'status':'failed','message':'Please provide loyalty_type'},status=status.HTTP_400_BAD_REQUEST)
        user=request.user
        customer=Customer.objects.get(user=user)
        try:
              profile=LoyaltyProfile.objects.get(customer=customer)
        except:
            return Response({'status':'failed','message':'No loyalty profile found'},status=status.HTTP_400_BAD_REQUEST)
        try:
            loyalty_type=Loyalty.objects.get(type=loyalty_type)
        except:
            return Response({'status':'failed','message':'Invalid loyalty type'},status=status.HTTP_400_BAD_REQUEST)
        profile.current_points+=loyalty_type.points
        
        profile.maximum_points=max(profile.maximum_points,profile.current_points)
        profile.calculate_current_tier()
        profile.save()
        serializer=LoyaltyProfileSerializer(profile)
        return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
    

        