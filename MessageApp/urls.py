from django.urls import path
from MessageApp import views

urlpatterns = [
      path('adminMessage/', views.AdminMessages, name='adminMessage/'),
      path('providerMessage/', views.ProviderMessages, name='adminMessage/'),
      path('userMessage/', views.UsersMessages, name='adminMessage/'),
]