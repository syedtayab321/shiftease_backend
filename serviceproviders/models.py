from django.db import models

# Create your models here.
class ServiceProviders(models.Model):
    email = models.EmailField(max_length=254)
    company_name = models.CharField(max_length=254)
    location = models.CharField(max_length=200)
    service = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=6)
    password = models.CharField(max_length=200)
    request_status = models.CharField(max_length=20)
    def __str__(self):
        return self.email

class PackagesModel(models.Model):
    company_email=models.EmailField(max_length=254)
    package_name = models.CharField(max_length=254)
    package_service = models.CharField(max_length=200)
    package_price = models.IntegerField()

class AddTeamModel(models.Model):
    company_email = models.EmailField(max_length=254)
    team_name = models.CharField(max_length=254)
    team_member_email = models.EmailField(max_length=254)
    team_member_name = models.CharField(max_length=254)
    team_member_role = models.CharField(max_length=200)
    team_member_phone = models.CharField(max_length=200)
    team_member_cnic = models.CharField(max_length=20)