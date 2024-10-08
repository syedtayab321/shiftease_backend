from django.db import models
class ServiceProviders(models.Model):
    email = models.EmailField(max_length=254)
    company_name = models.CharField(max_length=254)
    location = models.CharField(max_length=200)
    service = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=6)
    password = models.CharField(max_length=200)
    request_status = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='images/company_profiles')
    def __str__(self):
        return self.email

class PackagesModel(models.Model):
    company_id=models.IntegerField()
    package_name = models.CharField(max_length=254)
    package_service = models.CharField(max_length=200)
    package_description=models.CharField(max_length=1000)
    package_price = models.IntegerField()
    package_image = models.ImageField(upload_to='images/packages_images')

class AddTeamModel(models.Model):
    company_id = models.IntegerField()
    team_name = models.CharField(max_length=254)
    team_member_email = models.EmailField(max_length=254)
    team_member_name = models.CharField(max_length=254)
    team_member_role = models.CharField(max_length=200)
    team_member_phone = models.CharField(max_length=200)
    team_member_cnic = models.CharField(max_length=20)

class OrderRequestsModal(models.Model):
    client_name=models.CharField(max_length=1000)
    location=models.CharField(max_length=1000)
    service_date=models.DateField()
    package_name=models.CharField(max_length=1000,default='')
    package_id=models.CharField(max_length=1000,default='')
    package_price=models.CharField(max_length=1000,default='')
    Company_id=models.CharField(max_length=1000,default='')
    request_status=models.CharField(max_length=100)
    OrderPersonId=models.CharField(max_length=1000)

class ApprovedOrdersModal(models.Model):
    Company_id=models.CharField(max_length=1000,default='')
    client_name=models.CharField(max_length=1000)
    location=models.CharField(max_length=1000)
    service_date=models.DateField()
    package_id=models.CharField(max_length=1000,default='')
    package_price=models.CharField(max_length=1000,default='')
    team_name=models.CharField(max_length=1000)
    order_status=models.CharField(max_length=100,default='')