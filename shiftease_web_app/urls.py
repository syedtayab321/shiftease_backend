from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('providerapis/', include('serviceproviders.urls')),
    path('adminapis/', include('Admin.urls')),
    path('MessageApis/', include('MessageApp.urls')),
    path('teamportalApis/', include('TeamPortal.urls')),
    path('Providerforgotpassword/', include('ForgotPassword.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)