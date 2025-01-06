import logging
from django.core.mail import send_mail
from Admin.models import Users
from serviceproviders import models as ProvidersModals
from Admin import models as AdminModels
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
            return Response('UserData Deleted Successfully')
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
            images = request.FILES.getlist('images')
            ad_data = {key: value for key, value in request.data.items() if key != 'images'}
            rent_ad_serializer = AdminSerializer.RentAdSerializer(data=ad_data)
            if rent_ad_serializer.is_valid():
                rent_ad = rent_ad_serializer.save()
                for image in images:
                    image_serializer = AdminSerializer.RentAdImageSerializer(
                        data={'rent_ad': rent_ad.id, 'image': image})
                    if image_serializer.is_valid():
                        image_serializer.save()
                    else:
                        print(image_serializer.errors)
                        return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                return Response(AdminSerializer.RentAdSerializer(rent_ad).data, status=status.HTTP_201_CREATED)
            else:
                print(rent_ad_serializer.errors)
                return Response(rent_ad_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'GET':
        rent_ad_id = request.GET.get('rent_id')
        userEmail = request.GET.get('userMail')
        if rent_ad_id:
            try:
                rent_ad = AdminModels.RentAd.objects.get(id=rent_ad_id)
                rent_ad_serializer = AdminSerializer.RentAdSerializer(rent_ad)
                return Response(rent_ad_serializer.data, status=status.HTTP_200_OK)
            except AdminModels.RentAd.DoesNotExist:
                return Response({'error': 'Rent Ad not found'}, status=status.HTTP_404_NOT_FOUND)
        if userEmail:
            try:
                rent_ad = AdminModels.RentAd.objects.get(ownerEmail=userEmail)
                rent_ad_serializer = AdminSerializer.RentAdSerializer(rent_ad)
                return Response(rent_ad_serializer.data, status=status.HTTP_200_OK)
            except AdminModels.RentAd.DoesNotExist:
                return Response({'error': 'Rent Ad not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            rent_ads = AdminModels.RentAd.objects.all()
            rent_ad_serializer = AdminSerializer.RentAdSerializer(rent_ads, many=True)
            return Response(rent_ad_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        rent_ad_id = request.GET.get('rent_id')
        if not rent_ad_id:
            return Response({'error': 'Rent Ad ID is required for updating'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            rent_ad = AdminModels.RentAd.objects.get(id=rent_ad_id)
            images = request.FILES.getlist('images')
            ad_data = {key: value for key, value in request.data.items() if key != 'images'}
            rent_ad_serializer = AdminSerializer.RentAdSerializer(rent_ad, data=ad_data, partial=True)
            if rent_ad_serializer.is_valid():
                updated_rent_ad = rent_ad_serializer.save()

                for image in images:
                    image_serializer = AdminSerializer.RentAdImageSerializer(
                        data={'rent_ad': updated_rent_ad.id, 'image': image}
                    )
                    if image_serializer.is_valid():
                        image_serializer.save()
                    else:
                        return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response(AdminSerializer.RentAdSerializer(updated_rent_ad).data, status=status.HTTP_200_OK)
            else:
                return Response(rent_ad_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AdminModels.RentAd.DoesNotExist:
            return Response({'error': 'Rent Ad not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        rent_ad_id = request.GET.get('rent_id')
        if not rent_ad_id:
            return Response({'error': 'Rent Ad ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            rent_ad = AdminModels.RentAd.objects.get(id=rent_ad_id)
            rent_ad.delete()
            return Response({'message': 'Rent Ad deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except AdminModels.RentAd.DoesNotExist:
            return Response({'error': 'Rent Ad not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
