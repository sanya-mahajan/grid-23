from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from loyalties.models import *
from loyalties.serializers import *

class CreateTransaction(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        try:
            amount=request.data['amount']
        except:
            return Response({'status':'failed','message':'Please provide amount'},status=status.HTTP_400_BAD_REQUEST)
        user=request.user
        try:
            customer=Customer.objects.get(user=user)
        except:
            return Response({'status':'failed','message':'Invalid user type'},status=status.HTTP_400_BAD_REQUEST)
        try:
              profile=LoyaltyProfile.objects.get(customer=customer)
        except:
            return Response({'status':'failed','message':'No loyalty profile found'},status=status.HTTP_400_BAD_REQUEST)
        try:
            loyalty_type=Loyalty.objects.get(type="PURCHASE")
        except:
            return Response({'status':'failed','message':'Invalid loyalty type'},status=status.HTTP_400_BAD_REQUEST)
        transaction=Transaction.objects.create(customer=customer,amount=amount)
        profile.current_points+=loyalty_type.points
        profile.maximum_points=max(profile.maximum_points,profile.current_points)
        profile.calculate_current_tier()
        profile.save()
        serializer=TransactionSerializer(transaction)
        return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
    

class GetTransactionHistory(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    def get(self,request):
        user=request.user
        try:
            customer=Customer.objects.get(user=user)
        except:
            return Response({'status':'failed','message':'Invalid user type'},status=status.HTTP_400_BAD_REQUEST)
        transactions=Transaction.objects.filter(customer=customer).order_by('-date')
        serializer=TransactionSerializer(transactions,many=True)
        return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        