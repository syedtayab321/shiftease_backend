from rest_framework import serializers
from Admin.models import Users,HouseRentAd,OfficeRentAd,ApartmentRentAd

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class HouseRentAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseRentAd
        fields = '__all__'

class OfficeRentAdSerializer(serializers.ModelSerializer):
     class Meta:
         model = OfficeRentAd
         fields = '__all__'

class ApartmentRentAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentRentAd
        fields = '__all__'
