"""URL-конфигурация для проекта Yatube API."""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(
        'admin/',
        admin.site.core_admin_site
        if hasattr(admin.site, 'core_admin_site') else admin.site.urls
    ),
    path('api/', include('api.urls')),
]
