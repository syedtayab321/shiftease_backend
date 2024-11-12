from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    users_uid = models.CharField(max_length=1000)
    status = models.CharField(max_length=200, default='Active')


class RentAd(models.Model):
    # Common fields
    title = models.CharField(max_length=200, blank=True, null=True)
    propertyType = models.CharField(max_length=20)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    price_per_month = models.CharField(max_length=200)
    ownerName = models.CharField(max_length=200)
    ownerNumber = models.CharField(max_length=200)
    ownerEmail = models.EmailField(max_length=200)
    requestStatus = models.CharField(max_length=200)
    furnishing = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)

    # Fields specific to House
    houseType = models.CharField(max_length=200, blank=True, null=True)
    builtYear = models.CharField(max_length=4, blank=True, null=True)
    bedrooms = models.CharField(max_length=200, blank=True, null=True)
    bathrooms = models.CharField(max_length=200, blank=True, null=True)
    area = models.CharField(max_length=200, blank=True, null=True)

    # Fields specific to Office
    officeType = models.CharField(max_length=200, blank=True, null=True)
    officeSize = models.CharField(max_length=200, blank=True, null=True)
    floorNumber = models.CharField(max_length=200, blank=True, null=True)
    buildingType = models.CharField(max_length=200, blank=True, null=True)

    # Fields specific to Apartment
    apartmentType = models.CharField(max_length=200, blank=True, null=True)
    apartmentSize = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.propertyType} for Rent in {self.city}, {self.country} - {self.price_per_month}"


class RentAdImage(models.Model):
    rent_ad = models.ForeignKey(RentAd, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="images/RentProperties/")

    def __str__(self):
        return f"Image for {self.rent_ad}"
