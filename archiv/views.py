from django.views.generic import TemplateView

from browsing.utils import (
    GenericListView,
    BaseDetailView,
    BaseCreateView,
    BaseUpdateView,
)
from archiv.forms import PlaceForm
from archiv.models import Person, Place, Book
from archiv.tables import BookTable


class StartView(TemplateView):
    template_name = "archiv/index.html"


class PersonListView(GenericListView):
    model = Person
    init_columns = [
        "id",
        "name",
    ]
    enable_merge = True


class PersonDetailView(BaseDetailView):
    model = Person


class PersonCreate(BaseCreateView):

    model = Person


class PersonUpdate(BaseUpdateView):

    model = Person


class PlaceListView(GenericListView):
    model = Place
    init_columns = [
        "id",
        "name",
    ]
    enable_merge = False


class PlaceCreate(BaseCreateView):

    model = Place
    form_class = PlaceForm


class PlaceUpdate(BaseUpdateView):

    model = Place
    form_class = PlaceForm


class PlaceDetailView(BaseDetailView):
    model = Place


class BookListView(GenericListView):
    h1 = "Stöbere in den Super Büchern"
    model = Book
    table_class = BookTable
    init_columns = [
        "id",
        "author",
        "name",
    ]
    enable_merge = False


class BookDetailView(BaseDetailView):
    model = Book


class BookCreate(BaseCreateView):

    model = Book


class BookUpdate(BaseUpdateView):

    model = Book
