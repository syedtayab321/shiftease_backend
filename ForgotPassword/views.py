import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from serviceproviders.models import ServiceProviders as Provider
from .serializers import ForgotPasswordSerializer, VerifyCodeSerializer, ResetPasswordSerializer

class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                provider = Provider.objects.get(email=email)
                
                # Remove any existing verification code
                provider.verification_code = None
                
                # Generate a new 6-digit verification code
                verification_code = random.randint(100000, 999999)
                provider.verification_code = verification_code
                provider.save()
                
                # Send the verification code via email
                send_mail(
                    'Password Reset Code',
                    f'Your verification code is {verification_code}',
                    'syedhussain4508@gmail.com',
                    [email],
                )
                return Response({'message': 'Verification code sent to email.'}, status=status.HTTP_200_OK)
            except Provider.DoesNotExist:
                return Response({'error': 'Email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

import logging
logger = logging.getLogger(__name__)

class VerifyCodeView(APIView):
    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            code = serializer.validated_data['code']
            try:
                provider = Provider.objects.get(email=email)
                if str(provider.verification_code) == str(code):
                    return Response({'message': 'Code verified. You can reset your password.'}, status=status.HTTP_200_OK)
                print(provider)
                return Response({'error': 'Invalid verification code.'}, status=status.HTTP_400_BAD_REQUEST)
            except Provider.DoesNotExist:
                return Response({'error': 'Email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            logger.error(f"Serializer errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            new_password = serializer.validated_data['new_password']
            try:
                provider = Provider.objects.get(email=email)
                provider.set_password(new_password)
                provider.verification_code = None
                provider.save()
                return Response({'message': 'Password reset successfully.'}, status=status.HTTP_200_OK)
            except Provider.DoesNotExist:
                return Response({'error': 'Email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
