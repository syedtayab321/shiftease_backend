from django.core.mail import send_mail
from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import ServiceProvidersSerializer,UserProfileSerializer,PackageSerializer,AddTeamSerializer
from .models import ServiceProviders,PackagesModel,AddTeamModel
from rest_framework.parsers import MultiPartParser, FormParser
@api_view(['POST'])
def Providersignup(request):
    serializer = ServiceProvidersSerializer(data=request.data)
    if serializer.is_valid():
        # Extract the email from the validated data
        email = serializer.validated_data.get('email')

        # Check if the email already exists in the database
        if ServiceProviders.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Save the new service provider data
        serializer.save()

        # Extract the validated data for email
        data = serializer.validated_data
        company_name = data.get('company_name')
        location = data.get('location')
        services = data.get('service')
        mobile_no = data.get('mobile_no')
        zipcode = data.get('zipcode')

        # Prepare the email content
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

    # Check if the email and password are provided
    if not email or not password:
        return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = ServiceProviders.objects.get(email=email)

        # Verify the password
        if password != user.password:
            return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare user data to send back
        user_data = {
            'email': user.email,
            'companyname': user.company_name,
            'requeststatus': user.request_status
        }

        return Response(user_data, status=status.HTTP_200_OK)

    except ServiceProviders.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        # Log the exception or print it for debugging purposes
        print(f"An error occurred: {e}")
        return Response({'error': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT'])
def profile_data(request):
    email = request.GET.get('email')

    if request.method == 'GET':
        if email:
            try:
                user_profile = ServiceProviders.objects.get(email=email)
                serializer = UserProfileSerializer(user_profile)
                return Response(serializer.data)
            except ServiceProviders.DoesNotExist:
                return Response({'error': 'User not found'}, status=404)
        return Response({'error': 'Email parameter is required'}, status=400)

    elif request.method == 'PUT':
        if email:
            try:
                user_profile = ServiceProviders.objects.get(email=email)
                data = request.data
                serializer = UserProfileSerializer(user_profile, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            except ServiceProviders.DoesNotExist:
                return Response({'error': 'User not found'}, status=404)
        return Response({'error': 'Email parameter is required'}, status=400)


@api_view(['GET','PUT','DELETE','POST'])
def PackagesData(request):
    email = request.GET.get('email')
    id = request.GET.get('id')
    if request.method == 'GET':
       try:
           if email:
               packagedata = PackagesModel.objects.filter(company_email=email)
               serializer = PackageSerializer(packagedata, many=True)
               return Response(serializer.data)
           elif id:
               packagedata = PackagesModel.objects.get(id=id)
               serializer = PackageSerializer(packagedata,many=True)
               return Response(serializer.data)
           else:
               packagedata = PackagesModel.objects.all()
               serializer = PackageSerializer(packagedata,many=True)
               return Response(serializer.data,status=status.HTTP_200_OK)
       except PackagesModel.DoesNotExist:
            return Response({'error': 'Data not found'}, status=404)

    elif request.method == 'POST':
        try:
            serializer = PackageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        try:
            PackagesModel.objects.filter(id=id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'PUT':
        try:
            packagedata = PackagesModel.objects.get(id=id)
            data = request.data
            serializer = PackageSerializer(packagedata, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except PackagesModel.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)


@api_view(['GET','PUT','DELETE','POST'])
def TeamData(request):
    email = request.GET.get('email')
    id = request.GET.get('id')
    if request.method == 'GET':
        try:
            if email:
                teamdata = AddTeamModel.objects.filter(company_email=email)
                serializer = AddTeamSerializer(teamdata, many=True)
                return Response(serializer.data)
            elif id:
                teamdata = AddTeamModel.objects.get(id=id)
                serializer = AddTeamSerializer(teamdata)
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
                    print("Serializer Errors:", serializer.errors)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=500)

    elif request.method == 'DELETE':
        try:
            AddTeamModel.objects.filter(id=id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'PUT':
        try:
            teamdata = AddTeamModel.objects.get(id=id)
            data = request.data
            serializer = AddTeamSerializer(teamdata, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except AddTeamModel.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
