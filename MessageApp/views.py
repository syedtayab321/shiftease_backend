from MessageApp import models as MessageModels
from MessageApp import serializers as MessageSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def AdminMessages(request):
    if request.method == 'POST':
        message_data = MessageSerializers.AdminMessageSerializer(data=request.data)
        ProviderMessage_data = MessageSerializers.ProviderMessageSerializer(data=request.data)
        if message_data.is_valid():
            message_data.save()
            if ProviderMessage_data.is_valid():
                ProviderMessage_data.save()
                return Response('Message Send Sucessfully', status=status.HTTP_200_OK)
            return Response(ProviderMessage_data.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(message_data.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        receiverName = request.GET.get('receiverName')
        senderName = request.GET.get('senderName')
        try:
            if receiverName:
                messageData = MessageModels.AdminMessageModal.objects.filter(receiverName = receiverName, senderName = senderName)
                serializer = MessageSerializers.AdminMessageSerializer(messageData, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                messageData = MessageModels.AdminMessageModal.objects.all()
                serializer = MessageSerializers.AdminMessageSerializer(messageData, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=500)
    if request.method == 'DELETE':
        messageId = request.GET.get('messageId')
        try:
            MessageModels.AdminMessageModal.objects.filter(id=messageId).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response('Please Provide some data')


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def ProviderMessages(request):
    if request.method == 'POST':
        receiverName = request.data.get('receiverName')
        ProviderMessage_data = MessageSerializers.ProviderMessageSerializer(data=request.data)
        AdminMessage_data = MessageSerializers.AdminMessageSerializer(data=request.data)
        UserMessage_data = MessageSerializers.UserMessageSerializer(data=request.data)

        if ProviderMessage_data.is_valid():
            ProviderMessage_data.save()
            if receiverName == 'Admin':
                if AdminMessage_data.is_valid():
                    AdminMessage_data.save()
                    return Response('Message Send Successfully', status=status.HTTP_200_OK)
                else:
                    if UserMessage_data.is_valid():
                        UserMessage_data.save()
                        return Response('Message Send Successfully', status=status.HTTP_200_OK)

            return Response('Admin Data Is not Valid', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(ProviderMessage_data.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        receiverName = request.GET.get('receiverName')
        senderName = request.GET.get('senderName')
        try:
            if receiverName:
                messageData = MessageModels.ProviderMessageModal.objects.filter(receiverName=receiverName, senderName = senderName)
                serializer = MessageSerializers.ProviderMessageSerializer(messageData, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                messageData = MessageModels.ProviderMessageModal.objects.all()
                serializer = MessageSerializers.ProviderMessageSerializer(messageData, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=500)
    if request.method == 'DELETE':
        messageId = request.GET.get('messageId')
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

    if request.method == 'GET':
        receiverName = request.GET.get('receiverName')
        try:
            messageData = MessageModels.UserMessageModal.objects.filter(receiverName=receiverName)
            serializer = MessageSerializers.UserMessageSerializer(messageData, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=500)

    if request.method == 'DELETE':
        messageId = request.GET.get('messageId')
        try:
            MessageModels.UserMessageModal.objects.filter(id=messageId).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response('Please Provide some data')
