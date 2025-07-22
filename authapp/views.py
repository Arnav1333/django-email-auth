from django.shortcuts import render
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User,OTP
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful. Please verify your email.'}, status=201)
        return Response(serializer.errors, status=400)
    
class RequestOTPView(APIView):
    def post(self,request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
        except:
            return Response({'error':'User not found!'},status=404)
        
        otp_code = f"{random.randint(100000,999999)}"
        OTP.objects.create(user=user,code=otp_code)

        print(f"[Mock Email] OTP for {email}: {otp_code}")  
        return Response({'message': 'OTP sent to your email.'}, status=200)

class VerifyOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        code = request.data.get('otp')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=404)

        try:
            otp = OTP.objects.filter(user=user, code=code).latest('created_at')
        except OTP.DoesNotExist:
            return Response({'error': 'Invalid OTP.'}, status=400)

        if otp.is_expired():
            return Response({'error': 'OTP expired.'}, status=400)

        user.is_verified = True
        user.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'Login successful.',
            'token': str(refresh.access_token)
        }, status=200)