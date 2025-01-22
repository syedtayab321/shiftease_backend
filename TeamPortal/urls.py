from django.urls import path
from TeamPortal import views

urlpatterns = [
    path('teamLogin/', views.TeamLeaderLogin, name='teamlogin'),
    path('teamAssignedTasks/', views.get_approved_orders, name='teamAssignedTasks'),
]
