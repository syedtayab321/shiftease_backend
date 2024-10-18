from django.urls import path
from Admin import views

urlpatterns = [
    path('providersdata/', views.ProvidersData, name='providersdata'),
    path('accountApproval/', views.AccountApproval, name='accountApproval'),
    path('UserSignUp/', views.SignUpUsers, name='UserSignUp'),
    path('HouseSellingAdData/', views.HouseRentAdData, name='HouseSellingRentAd'),
    path('ApartmentSellingAdData/', views.ApartmentRentAdData, name='ApartmentSellingRentAd'),
    path('OfficeSellingAdData/', views.OfficeRentAdData, name='OfficeSellingRentAd'),
]
