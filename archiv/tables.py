import django_tables2

from archiv.models import Book


class BookTable(django_tables2.Table):

    name = django_tables2.LinkColumn(verbose_name="Title")
    author = django_tables2.columns.ManyToManyColumn(verbose_name="Authors")
    place_of_publication = django_tables2.columns.ManyToManyColumn(verbose_name="Place")

    class Meta:
        model = Book
        sequence = (
            "author",
            "name",
            "place_of_publication",
        )
