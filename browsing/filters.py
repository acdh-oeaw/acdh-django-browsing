import django_filters


def get_generic_filter(model_class):

    class GenericFilter(django_filters.FilterSet):

        class Meta:
            model = model_class
            fields = "__all__"

    return GenericFilter
