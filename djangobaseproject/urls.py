from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("archiv.urls", namespace="archiv")),
    path("admin/", admin.site.urls),
    path("browsing", include("browsing.urls", namespace="browsing")),
]
