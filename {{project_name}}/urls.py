# https://docs.djangoproject.com/en/5.0/topics/http/urls/

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("landingpage.urls")),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]

if settings.ADMIN_ENABLED:
    urlpatterns += [
        path("admin/", admin.site.urls),
    ]
