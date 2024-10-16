"""URL configuration for sm_api."""

from django.contrib import admin
from django.urls import include, path

from .views import root_route

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'dj-rest-auth/registration/',
        include('dj_rest_auth.registration.urls'),
    ),
    path('', include('core.urls')),
]
