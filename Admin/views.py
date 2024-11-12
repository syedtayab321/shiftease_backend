import logging
from django.core.mail import send_mail
from Admin.models import Users
from serviceproviders import models as ProvidersModals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serviceproviders import serializers as ProviderSerializer
from Admin import serializers as AdminSerializer
from rest_framework import status


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def ProvidersData(request):
    if request.method == 'GET':
        try:
            userdata = ProvidersModals.ServiceProviders.objects.all()
            serializer = ProviderSerializer.ServiceProvidersSerializer(userdata, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response('No Data Found')
    elif request.method == 'DELETE':
        try:
            ProvidersModals.ServiceProviders.objects.filter(id=request.GET['id']).delete()
            return Response('UserData Deleted Sucessfully')
        except Exception as e:
            return Response('No Data Found')


logger = logging.getLogger(__name__)


@api_view(['POST'])
def AccountApproval(request):
    serializer = ProviderSerializer.AccountApprovalSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        id = serializer.validated_data.get('id')
        status_value = serializer.validated_data.get('request_status')
        try:
            num_updated = ProvidersModals.ServiceProviders.objects.filter(email=email).update(
                request_status=status_value)
            if num_updated == 0:
                logger.warning(f'No user found with email: {email}')
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                subject = 'Account Approval'
                message = f"""
                         Dear User ,
                         Your account has been {status_value}
                         Thank you for your attention.
                         Best regards,
                         ShiftEase
                         """
                from_email = 'syedhussain4508@gmail.com'
                to_email = email
                send_mail(subject, message, from_email, [to_email]),
                return Response({'message': 'Status updated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f'Error during approval: {e}')
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        logger.warning(f'Serializer errors: {serializer.errors}')
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def SignUpUsers(request):
    if request.method == 'POST':
        try:
            serializer = AdminSerializer.UserSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'GET':
        userEmail = request.GET.get('email')
        userPassword = request.GET.get('password')
        try:
            if userEmail:
                Userdata = Users.objects.filter(email=userEmail, password=userPassword)
                serializerData = AdminSerializer.UserSerializer(Userdata, many=True)
                return Response(serializerData.data, status=status.HTTP_200_OK)
            else:
                Userdata = Users.objects.all()
                serializerData = AdminSerializer.UserSerializer(Userdata, many=True)
                return Response(serializerData.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        userId = request.GET.get('UserId')
        try:
            Users.objects.filter(id=userId).delete()
            return Response({"message": "Data Deleted Successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    return Response({"message": "Invalid method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST', 'GET', 'DELETE', 'PUT'])
def RentAdsData(request):
    if request.method == 'POST':
        try:
            # Separate image data from other fields
            image_data = request.FILES.getlist('images')
            ad_data = {key: value for key, value in request.data.items() if key != 'images'}
            # Serialize and save RentAd (excluding images for now)
            rent_ad_serializer = AdminSerializer.RentAdSerializer(data=ad_data)
            if rent_ad_serializer.is_valid():
                rent_ad = rent_ad_serializer.save()
                for image in image_data:
                    image_serializer = AdminSerializer.RentAdImage(data={'rent_ad': rent_ad.id, 'image': image})
                    if image_serializer.is_valid():
                        image_serializer.save()
                    else:
                        print(image_serializer.errors)
                        return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                full_data = AdminSerializer.RentAdSerializer(rent_ad).data
                return Response(full_data, status=status.HTTP_201_CREATED)
            else:
                 print(rent_ad_serializer.errors)
                 return Response(rent_ad_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
              return Response({'error': f"Error in creating rent ad: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
