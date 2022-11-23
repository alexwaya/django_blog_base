from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('projectApp.urls')),

    path('', include('userblog.urls')),
     
    #path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]
