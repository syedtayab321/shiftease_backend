from rest_framework import serializers
from .models import ServiceProviders,PackagesModel,AddTeamModel

class ServiceProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProviders
        fields = '__all__'

class AccountApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProviders
        fields = ['id','email','request_status']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProviders
        fields = '__all__'

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackagesModel
        fields = '__all__'

class AddTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddTeamModel
        fields = '__all__'