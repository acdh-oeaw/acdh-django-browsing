from django.views.generic import TemplateView

from browsing.utils import GenericListView, BaseDetailView
from archiv.models import Person
from archiv.filters import PersonListFilter
from archiv.forms import PersonFilterFormHelper


class StartView(TemplateView):
    template_name = "archiv/index.html"


class PersonListView(GenericListView):
    model = Person
    filter_class = PersonListFilter
    formhelper_class = PersonFilterFormHelper
    init_columns = [
        "name",
    ]
    enable_merge = False


class PersonDetailView(BaseDetailView):
    model = Person
