from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    users_uid = models.CharField(max_length=1000)


class HouseRentAd(models.Model):
    houseImage = models.ImageField(upload_to="images/RentHouse/")
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    houseType = models.CharField(max_length=200)
    builtYear = models.CharField(max_length=200)
    bedrooms = models.CharField(max_length=200)
    bathrooms = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    furnishing = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    houseDescription = models.CharField(max_length=200)
    ownerName = models.CharField(max_length=200)
    ownerNumber = models.CharField(max_length=200)
    ownerEmail = models.CharField(max_length=200)
    RequestStatus = models.CharField(max_length=200)


class OfficeRentAd(models.Model):
    officeImage = models.ImageField(upload_to="images/RentOffice/")
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    desciption = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    officeType = models.CharField(max_length=200)
    officeSize = models.CharField(max_length=200)
    floorNumber = models.CharField(max_length=200)
    buildingType = models.CharField(max_length=200)
    ownerName = models.CharField(max_length=200)
    ownerNumber = models.CharField(max_length=200)
    ownerEmail = models.EmailField(max_length=200)
    RequestStatus = models.CharField(max_length=200)


class ApartmentRentAd(models.Model):
    apartmentImage = models.ImageField(upload_to="images/RentApartment/")
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    desciption = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    apartmentType = models.CharField(max_length=200)
    aprtmentSize = models.CharField(max_length=200)
    floorNumber = models.CharField(max_length=200)
    bedrooms = models.CharField(max_length=200)
    bathrooms = models.CharField(max_length=200)
    furnishing = models.CharField(max_length=200)
    ownerName = models.CharField(max_length=200)
    ownerNumber = models.CharField(max_length=200)
    ownerEmail = models.EmailField(max_length=200)
    RequestStatus = models.CharField(max_length=200)
