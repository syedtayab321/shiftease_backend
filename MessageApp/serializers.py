from rest_framework import serializers
from MessageApp import models as MessageModals


class AdminMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModals.AdminMessageModal
        fields = '__all__'


class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModals.UserMessageModal
        fields = '__all__'


class ProviderMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModals.ProviderMessageModal
        fields = '__all__'
