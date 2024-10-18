from MessageApp import models as MessageModels
from MessageApp import serializers as MessageSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def AdminMessages(request):
    if request.method == 'POST':
        message_data = MessageSerializers.AdminMessageSerializer(request=request.data)
        if message_data.is_valid():
            message_data.save()
            return Response('Message Send Sucessfully', status=status.HTTP_200_OK)
        else:
            return Response(message_data.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response('Please Provide some data')


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def ProviderMessages(request):
    if request.method == 'POST':
        message_data = MessageSerializers.ProviderMessageSerializer(data=request.data)
        if message_data.is_valid():
            message_data.save()
            return Response('Message Send Sucessfully', status=status.HTTP_200_OK)
        else:
            return Response(message_data.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        recevierName = request.GET.get('receiverName')
        try:
            messageData = MessageModels.ProviderMessageModal.objects.filter(receiverName=recevierName)
            serializer = MessageSerializers.ProviderMessageSerializer(messageData, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=500)
    if request.method == 'DELETE':
        messageId=request.GET.get('messageId')
        try:
            MessageModels.ProviderMessageModal.objects.filter(id=messageId).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response('Please Provide some data')


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def UsersMessages(request):
    if request.method == 'POST':
        message_data = MessageSerializers.UserMessageSerializer(data=request.data)
        if message_data.is_valid():
            message_data.save()
            return Response('Message Send Sucessfully', status=status.HTTP_200_OK)
        else:
            return Response(message_data.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response('Please Provide some data')
