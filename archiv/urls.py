from django.urls import path

from archiv.views import StartView, PersonDetailView, PersonListView

app_name = "archiv"

urlpatterns = [
    path("", StartView.as_view(), name="home"),
    path("persons/", PersonListView.as_view(), name="person_list"),
    path(
        "persons/detail/<int:pk>",
        PersonDetailView.as_view(),
        name="person_detail",
    ),
]
