from django.urls import path
from serviceproviders import views

urlpatterns = [
     path('signup/',views.Providersignup,name='signup'),
     path('login/',views.ProviderLogin,name='login'),
     path('providerOwnData/', views.ProvidersOwnData, name='providerOwnData'),
     path('packagesdata/', views.PackagesData, name='packagesdata'),
     path('teamdata/', views.TeamData, name='teamdata'),
     path('serviceBookingRequests/', views.ServiceBookingRequests, name='serviceBookingRequests'),
     path('ApprovedOrders/',views.OrderAprrovals,name='ApprovedOrders'),
     path('packagePayments/', views.PaymentAPI, name='payment_api'),
    ]