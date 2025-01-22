from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from serviceproviders import models as ProvidersModals
from serviceproviders import serializers as ProviderSerializer
from rest_framework import status


@api_view(['POST'])
def TeamLeaderLogin(request):
    email = request.data.get('email')
    occupation = request.data.get('team_member_occupation')

    if not email or not occupation:
        return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        team_member = ProvidersModals.AddTeamModel.objects.get(
            team_member_email=email,
            team_member_occupation=occupation
        )
        serializer = ProviderSerializer.AddTeamSerializer(team_member)

        return Response({'message': 'Login successful', 'team_member': serializer.data}, status=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_approved_orders(request):
    company_id = request.query_params.get('Company_id')
    team_name = request.query_params.get('team_name')

    if not company_id or not team_name:
        return Response({'error': 'Company_id and team_name are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        orders = ProvidersModals.ApprovedOrdersModal.objects.filter(Company_id=company_id, team_name=team_name)
        serializer = ProviderSerializer.OrderRequestApprovalSerializers(orders, many=True)
        return Response({'orders': serializer.data}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': 'An error occurred while fetching data', 'details': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
