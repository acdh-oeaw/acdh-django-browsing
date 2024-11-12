from django.views.generic import TemplateView

from browsing.utils import GenericListView, BaseDetailView
from archiv.models import Person, Place, Book


class StartView(TemplateView):
    template_name = "archiv/index.html"


class PersonListView(GenericListView):
    model = Person
    init_columns = [
        "name",
    ]
    enable_merge = False


class PersonDetailView(BaseDetailView):
    model = Person


class PlaceListView(GenericListView):
    model = Place
    init_columns = [
        "name",
    ]
    enable_merge = False


class PlaceDetailView(BaseDetailView):
    model = Place


class BookListView(GenericListView):
    model = Book
    init_columns = [
        "name",
    ]
    enable_merge = False


class BookDetailView(BaseDetailView):
    model = Book
