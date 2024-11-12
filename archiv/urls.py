from django.urls import path

from archiv.views import StartView

app_name = "archiv"

urlpatterns = [path("", StartView.as_view(), name="home")]
