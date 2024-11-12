from django.urls import path

from archiv import views

app_name = "archiv"

urlpatterns = [
    path("", views.StartView.as_view(), name="home"),
    path("persons/", views.PersonListView.as_view(), name="person_list"),
    path(
        "persons/detail/<int:pk>",
        views.PersonDetailView.as_view(),
        name="person_detail",
    ),
    path("places/", views.PlaceListView.as_view(), name="place_list"),
    path(
        "places/detail/<int:pk>",
        views.PlaceDetailView.as_view(),
        name="place_detail",
    ),
    path("books/", views.BookListView.as_view(), name="book_list"),
    path(
        "books/detail/<int:pk>",
        views.BookDetailView.as_view(),
        name="place_detail",
    ),
]
