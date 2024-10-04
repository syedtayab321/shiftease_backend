import logging
from django.core.mail import send_mail
from Admin.models import Users
from Admin.models import HouseRentAd as HouseModel
from serviceproviders.models import ServiceProviders
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serviceproviders.serializers import ServiceProvidersSerializer, AccountApprovalSerializer
from Admin.serializer import UserSerializer,HouseRentAdSerializer,OfficeRentAdSerializer,ApartmentRentAdSerializer
from rest_framework import status
@api_view(['GET','POST','PUT','DELETE'])
def ProvidersData(request):
    if request.method == 'GET':
        try:
            userdata = ServiceProviders.objects.all()
            serializer = ServiceProvidersSerializer(userdata, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response('No Data Found')
    elif request.method == 'DELETE':
        try:
            userdata = ServiceProviders.objects.filter(id=request.GET['id']).delete()
            return Response('UserData Deleted Sucessfully')
        except Exception as e:
            return Response('No Data Found')
logger = logging.getLogger(__name__)

@api_view(['POST'])
def AccountApproval(request):
    serializer = AccountApprovalSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        status_value = serializer.validated_data.get('request_status')
        try:
            num_updated = ServiceProviders.objects.filter(email=email).update(request_status=status_value)
            if num_updated == 0:
                logger.warning(f'No user found with email: {email}')
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
             #    email send after approval
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

@api_view(['POST','GET','PUT','DELETE'])
def SignUpUsers(request):
    if request.method == 'POST':
        print("Incoming data:", request.data)
        try:
            # Try to serialize the incoming data
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()  # Save the user data
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'GET':
        try:
            Userdata = Users.objects.all()
            serializerdata = UserSerializer(Userdata, many=True)
            return Response(serializerdata.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({"message": "Invalid method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET','PUT','DELETE'])
def HouseRentAd(request):
    email = request.data.get('ownerEmail', None)
    if request.method == 'POST':
            serializer = HouseRentAdSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        try:
            if email:
                HouseRentData = HouseModel.objects.filter(email=email)
                serializerData = HouseRentAdSerializer(HouseRentData, many=True)
                return Response(serializerData.data, status=status.HTTP_200_OK)
            else:
                HouseRentData = HouseModel.objects.all()
                serializerData = HouseRentAdSerializer(HouseRentData, many=True)
                return Response(serializerData.data, status=status.HTTP_200_OK)
        except Exception as e:
             print(e)
             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response("error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)