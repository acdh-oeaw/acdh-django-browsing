import django_tables2 as tables

from archiv.models import Book


class BookTable(tables.Table):

    author = tables.columns.ManyToManyColumn(verbose_name="Authors")
    place_of_publication = tables.columns.ManyToManyColumn(verbose_name="Place")

    class Meta:
        model = Book
        sequence = (
            "author",
            "name",
            "place_of_publication",
        )
        attrs = {"class": "table table-responsive table-hover"}
