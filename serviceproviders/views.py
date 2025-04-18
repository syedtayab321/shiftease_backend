from django.core.mail import send_mail
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import ServiceProvidersSerializer, UserProfileSerializer, PackageSerializer, AddTeamSerializer, \
    OrderRequestsSerializers, OrderRequestApprovalSerializers,PaymentSerializer
from .models import ServiceProviders, PackagesModel, AddTeamModel, OrderRequestsModal, ApprovedOrdersModal,Payment
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

@api_view(['POST'])
def Providersignup(request):
    serializer = ServiceProvidersSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        if ServiceProviders.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        # Extract the validated data for email
        data = serializer.validated_data
        company_name = data.get('company_name')
        location = data.get('location')
        services = data.get('service')
        mobile_no = data.get('mobile_no')
        zipcode = data.get('zipcode')

        subject = 'New Service Provider Signup'
        message = f"""
        Dear Admin,

        A new service provider has signed up with the following details:

        Company Name: {company_name}
        Location: {location}
        Services: {services}
        Mobile Number: {mobile_no}
        Zip Code: {zipcode}
        Email: {email}

        Thank you for your attention.

        Best regards,
        Your Company
        """
        from_email = 'syedhussain4508@gmail.com'
        to_email = 'syedhussain4508@gmail.com'

        try:
            send_mail(subject, message, from_email, [to_email])
        except Exception as e:
            # Log the error or handle it appropriately
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def ProviderLogin(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = ServiceProviders.objects.get(email=email)
        if password != user.password:
            return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
        user_data = ServiceProvidersSerializer(user)
        return Response(user_data.data, status=status.HTTP_200_OK)
    except ServiceProviders.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(f"An error occurred: {e}")
        return Response({'error': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT'])
def ProvidersOwnData(request):
    id = request.GET.get('id')
    if request.method == 'GET':
        if id:
            try:
                user_profile = ServiceProviders.objects.get(id=id)
                serializer = UserProfileSerializer(user_profile)
                return Response(serializer.data)
            except ServiceProviders.DoesNotExist:
                return Response({'error': 'User not found'}, status=404)
        return Response({'error': 'Email parameter is required'}, status=400)

    elif request.method == 'PUT':
        if id:
            try:
                user_profile = ServiceProviders.objects.get(id=id)
                data = request.data
                serializer = UserProfileSerializer(user_profile, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            except ServiceProviders.DoesNotExist:
                return Response({'error': 'User not found'}, status=404)
        return Response({'error': 'Email parameter is required'}, status=400)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def PackagesData(request):
    company_id = request.GET.get('company_id')
    package_id = request.GET.get('package_id')
    if request.method == 'GET':
        try:
            if company_id:
                packagedata = PackagesModel.objects.filter(company_id=company_id)
                if not packagedata.exists():
                    return Response({'error': 'No packages found for the given company_id'},
                                    status=status.HTTP_404_NOT_FOUND)
                serializer = PackageSerializer(packagedata, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif package_id:
                try:
                    packagedata = PackagesModel.objects.get(id=package_id)
                    serializer = PackageSerializer(packagedata)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except PackagesModel.DoesNotExist:
                    return Response({'error': 'No packages found for the given package_id'},
                                    status=status.HTTP_404_NOT_FOUND)
            else:
                packagedata = PackagesModel.objects.all()
                serializer = PackageSerializer(packagedata, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print(str(e))
            return Response({'error': 'An unexpected error occurred: ' + str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    elif request.method == 'POST':
        serializer = PackageSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': 'Failed to create package: ' + str(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'validation_error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if not package_id:
            return Response({'error': 'Package ID is required for updating'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            packagedata = PackagesModel.objects.get(id=package_id)
        except PackagesModel.DoesNotExist:
            return Response({'error': 'Package with the given ID not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PackageSerializer(packagedata, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': 'Failed to update package: ' + str(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'validation_error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if not package_id:
            return Response({'error': 'Package ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            packagedata = PackagesModel.objects.get(id=package_id)
            packagedata.delete()
            return Response({'message': 'Package deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except PackagesModel.DoesNotExist:
            return Response({'error': 'Package with the given ID not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'Failed to delete package: ' + str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def TeamData(request):
    member_id = request.GET.get('id')
    company_id = request.GET.get('company_id')
    if request.method == 'GET':
        try:
            if member_id:
                teamdata = AddTeamModel.objects.get(id=member_id)
                serializer = AddTeamSerializer(teamdata)
                return Response(serializer.data)
            elif company_id:
                teamdata = AddTeamModel.objects.filter(company_id=company_id)
                serializer = AddTeamSerializer(teamdata, many=True)
                return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    elif request.method == 'POST':
        email = request.data.get('team_member_email')
        cnic = request.data.get('team_member_cnic')
        try:
            if AddTeamModel.objects.filter(team_member_email=email).exists():
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            if AddTeamModel.objects.filter(team_member_cnic=cnic).exists():
                return Response({'error': 'CNIC already exists'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = AddTeamSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    elif request.method == 'DELETE':
        try:
            AddTeamModel.objects.filter(id=member_id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'PUT':
        try:
            teamdata = AddTeamModel.objects.get(id=member_id)
            data = request.data
            serializer = AddTeamSerializer(teamdata, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except AddTeamModel.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def ServiceBookingRequests(request):
    if request.method == 'POST':
        try:
            serializer = OrderRequestsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
    elif request.method == 'GET':
        try:
            ordersdata = OrderRequestsModal.objects.all()
            serializer = OrderRequestsSerializers(ordersdata, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    elif request.method == 'DELETE':
        request_id = request.GET.get('request_id')
        try:
            OrderRequestsModal.objects.filter(id=request_id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def OrderAprrovals(request):
    if request.method == 'POST':
        try:
            serializer = OrderRequestApprovalSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(request.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=500)

    elif request.method == 'GET':
        company_id = request.GET.get('company_id')
        try:
            if company_id:
                ordersdata = ApprovedOrdersModal.objects.filter(Company_id=company_id)
                serializer = OrderRequestApprovalSerializers(ordersdata, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                ordersdata = ApprovedOrdersModal.objects.all()
                serializer = OrderRequestApprovalSerializers(ordersdata, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=500)

    elif request.method == 'PUT':
        orderId = request.GET.get('order_id')
        try:
            ApprovedData = ApprovedOrdersModal.objects.get(id=orderId)
        except ApprovedOrdersModal.DoesNotExist:
            return Response({"error": "House Rent Ad not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderRequestApprovalSerializers(ApprovedData, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        orderId = request.GET.get('order_id')
        try:
            ApprovedOrdersModal.objects.filter(id=orderId).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class PaymentAPI(APIView):
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Payment saved successfully!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)