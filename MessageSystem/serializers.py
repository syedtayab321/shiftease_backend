from rest_framework import serializers
from MessageSystem import models as MessageModals

class AdminProviderMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModals.AdminProviderMessageModal
        fields = '__all__'

class AdminUserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModals.AdminUserMessageModal
        fields = '__all__'

class ProviderUserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModals.AdminUserMessageModal
        fields = '__all__'