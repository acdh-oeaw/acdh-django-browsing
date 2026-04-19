from django.views.generic import TemplateView

from archiv.forms import PlaceForm
from archiv.models import Book, Person, Place
from archiv.tables import BookTable
from browsing.utils import (
    BaseCreateView,
    BaseDetailView,
    BaseUpdateView,
    GenericListView,
)


class StartView(TemplateView):
    template_name = "archiv/index.html"


class PersonListView(GenericListView):
    model = Person
    init_columns = [
        "id",
        "name",
    ]
    enable_merge = True
    page_size_label = "Paginationsgröße"
    page_size_option = [10, 11, 12, 33]


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
