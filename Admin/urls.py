from django.urls import path
from Admin import views
urlpatterns = [
    path('userdata/',views.UserData,name='userdata'),
    path('accountApproval/',views.AccountApproval,name='accountApproval'),
    path('UserSignUp/',views.SignUpUsers,name='UserSignUp'),
]