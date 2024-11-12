import django_filters

from archiv.models import Person


class PersonListFilter(django_filters.FilterSet):

    class Meta:
        model = Person
        fields = "__all__"
