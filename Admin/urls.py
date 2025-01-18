from django.urls import path
from Admin import views

urlpatterns = [
    path('providersdata/', views.ProvidersData, name='providersdata'),
    path('accountApproval/', views.AccountApproval, name='accountApproval'),
    path('UserSignUp/', views.SignUpUsers, name='UserSignUp'),
    path('RentAdData/', views.RentAdsData, name='RentAdData'),
    path('RentAdApproval/', views.RentAdsApproval, name='RentAdApproval')
]
