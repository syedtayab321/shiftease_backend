from rest_framework import serializers
from Admin.models import Users, RentAd, RentAdImage,Complaint


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class RentAdImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentAdImage
        fields = ['rent_ad', 'image']


class RentAdSerializer(serializers.ModelSerializer):
    images = RentAdImageSerializer(many=True, read_only=True)

    class Meta:
        model = RentAd
        fields = [
            'id', 'title', 'propertyType', 'country', 'city', 'address', 'price_per_month', 'ownerName',
            'ownerNumber', 'ownerEmail', 'requestStatus', 'furnishing', 'Description',
            'houseType', 'builtYear', 'bedrooms', 'bathrooms', 'area',
            'officeType', 'officeSize', 'floorNumber', 'buildingType',
            'apartmentType', 'apartmentSize', 'images'
        ]


class RentAdApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentAd
        fields = ['id','ownerEmail','requestStatus']

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'