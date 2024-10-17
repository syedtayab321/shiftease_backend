from django.urls import path
from MessageSystem import views

urlpatterns = [
      path('adminMessage/', views.AdminMessages, name='adminMessage/'),
      path('providerMessage/', views.ProviderMessages, name='adminMessage/'),
      path('userMessage/', views.UsersMessages, name='adminMessage/'),
]