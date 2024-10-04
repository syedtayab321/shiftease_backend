from django.urls import path
from serviceproviders import views

urlpatterns = [
     path('signup/',views.Providersignup,name='signup'),
     path('login/',views.ProviderLogin,name='login'),
     path('profiledata/', views.profile_data, name='get_user_profile'),
     path('packagesdata/', views.PackagesData, name='packagesdata'),
     path('teamdata/', views.TeamData, name='teamdata'),
     path('serviceBookingRequests/', views.ServiceBookingRequests, name='serviceBookingRequests'),
    ]