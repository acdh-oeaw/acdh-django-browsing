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
    path("persons/create/", views.PersonCreate.as_view(), name="person_create"),
    path("persons/edit/<int:pk>", views.PersonUpdate.as_view(), name="person_edit"),
    path("places/", views.PlaceListView.as_view(), name="place_list"),
    path(
        "places/detail/<int:pk>",
        views.PlaceDetailView.as_view(),
        name="place_detail",
    ),
    path("places/create/", views.PlaceCreate.as_view(), name="place_create"),
    path("places/edit/<int:pk>", views.PlaceUpdate.as_view(), name="place_edit"),
    path("books/", views.BookListView.as_view(), name="book_list"),
    path(
        "books/detail/<int:pk>",
        views.BookDetailView.as_view(),
        name="book_detail",
    ),
    path("books/create/", views.BookCreate.as_view(), name="book_create"),
    path("books/edit/<int:pk>", views.BookUpdate.as_view(), name="book_edit"),
]
