import django_tables2
from django.utils.safestring import mark_safe
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from crispy_forms.helper import FormHelper

from django_tables2.export.views import ExportMixin

from browsing.filters import get_generic_filter

input_form = """
  <input type="checkbox" name="keep" value="{}" title="keep this"/> |
  <input type="checkbox" name="remove" value="{}" title="remove this"/>
"""


class MergeColumn(django_tables2.Column):
    """renders a column with to checkbox - used to select objects for merging"""

    def __init__(self, *args, **kwargs):
        super(MergeColumn, self).__init__(*args, **kwargs)

    def render(self, value):
        return mark_safe(input_form.format(value, value))


def get_entities_table(model_class):
    class GenericEntitiesTable(django_tables2.Table):
        id = django_tables2.LinkColumn(verbose_name="ID")
        merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

        class Meta:
            model = model_class
            attrs = {"class": "table table-hover table-striped table-condensed"}

    return GenericEntitiesTable


class GenericFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False


class GenericListView(ExportMixin, django_tables2.SingleTableView):
    filter_class = None
    formhelper_class = GenericFilterFormHelper
    context_filter_name = "filter"
    paginate_by = 50
    template_name = "browsing/generic_list.html"
    init_columns = [
        "id",
    ]
    enable_merge = False
    excluded_cols = []
    h1 = ""
    create_button_text = "Create new item"
    introduction = ""

    def get_filterset_class(self):
        if self.filter_class:
            return self.filter_class
        else:
            filter_class = get_generic_filter(self.model)
            return filter_class

    def get_table_class(self):
        if self.table_class:
            return self.table_class
        else:
            return get_entities_table(self.model)

    def get_all_cols(self):
        all_cols = {
            key: value.header for key, value in self.get_table().base_columns.items()
        }
        return all_cols

    def get_queryset(self, **kwargs):
        qs = super(GenericListView, self).get_queryset()
        filter_class = self.get_filterset_class()
        self.filter = filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs.distinct()

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        default_cols = self.init_columns
        all_cols = table.base_columns.keys()
        selected_cols = self.request.GET.getlist("columns") + default_cols
        exclude_vals = [x for x in all_cols if x not in selected_cols]
        table.exclude = exclude_vals
        return table

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context["enable_merge"] = self.enable_merge
        togglable_colums = {
            key: value
            for key, value in self.get_all_cols().items()
            if key not in self.init_columns and key not in self.exclude_columns
        }
        context["togglable_colums"] = togglable_colums
        context[self.context_filter_name] = self.filter
        context["docstring"] = f"{self.model.__doc__}"
        try:
            context["create_view_link"] = self.model.get_createview_url()
        except AttributeError:
            context["create_view_link"] = None
        model_name = self.model.__name__.lower()
        context["entity"] = model_name
        context["app_name"] = self.model._meta.app_label
        if self.h1:
            context["h1"] = self.h1
        else:
            context["h1"] = f"Browse {self.model._meta.verbose_name_plural}"
        context["create_button_text"] = self.create_button_text
        context["verbose_name"] = self.model._meta.verbose_name
        context["verbose_name_plural"] = self.model._meta.verbose_name_plural
        return context


class BaseDetailView(DetailView):
    model = None
    template_name = "browsing/generic_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["docstring"] = f"{self.model.__doc__}"
        context["class_name"] = f"{self.model.__name__}"
        context["app_name"] = f"{self.model._meta.app_label}"
        context["verbose_name"] = self.model._meta.verbose_name
        context["verbose_name_plural"] = self.model._meta.verbose_name_plural
        return context


class BaseCreateView(CreateView):
    model = None
    form_class = None
    template_name = "browsing/generic_create.html"

    def get_context_data(self, **kwargs):
        context = super(BaseCreateView, self).get_context_data()
        context["docstring"] = f"{self.model.__doc__}"
        context["class_name"] = f"{self.model.__name__}"
        return context


class BaseUpdateView(UpdateView):
    model = None
    form_class = None
    template_name = "browsing/generic_create.html"

    def get_context_data(self, **kwargs):
        context = super(BaseUpdateView, self).get_context_data()
        context["docstring"] = f"{self.model.__doc__}"
        context["class_name"] = f"{self.model.__name__}"
        return context


def model_to_dict(instance):
    """
    serializes a model.object to dict, including non editable fields as well as
    ManyToManyField fields
    """
    field_dicts = []
    for x in instance._meta.get_fields():
        f_type = "{}".format(type(x))
        field_dict = {
            "name": x.name,
            "help_text": getattr(x, "help_text", ""),
        }
        try:
            field_dict["extra_fields"] = x.extra
        except AttributeError:
            field_dict["extra_fields"] = None
        if "reverse_related" in f_type:
            values = getattr(instance, x.name, None)
            if values is not None:
                field_dict["value"] = values.all()
            else:
                field_dict["value"] = []
            if getattr(x, "related_name", None) is not None:
                field_dict["verbose_name"] = getattr(x, "related_name", x.name)
            else:
                field_dict["verbose_name"] = getattr(x, "verbose_name", x.name)
            field_dict["f_type"] = "REVRESE_RELATION"
        elif "related.ForeignKey" in f_type:
            field_dict["verbose_name"] = getattr(x, "verbose_name", x.name)
            field_dict["value"] = getattr(instance, x.name, "")
            field_dict["f_type"] = "FK"
        elif "TreeForeignKey" in f_type:
            field_dict["verbose_name"] = getattr(x, "verbose_name", x.name)
            field_dict["value"] = getattr(instance, x.name, "")
            field_dict["f_type"] = "FK"
        elif "related.ManyToManyField" in f_type:
            values = getattr(instance, x.name, None)
            if values is not None:
                field_dict["value"] = values.all()
            else:
                field_dict["value"] = []
            field_dict["verbose_name"] = getattr(x, "verbose_name", x.name)
            field_dict["f_type"] = "M2M"
        elif "fields.DateTimeField" in f_type:
            field_value = getattr(instance, x.name, "")
            field_dict["verbose_name"] = getattr(x, "verbose_name", x.name)
            field_dict["f_type"] = "DateTime"
            if field_value:
                field_dict["value"] = field_value.strftime("%Y-%m-%d %H:%M:%S")
        else:
            field_dict["verbose_name"] = getattr(x, "verbose_name", x.name)
            field_dict["value"] = f"{getattr(instance, x.name, '')}"
            field_dict["f_type"] = "SIMPLE"
        field_dicts.append(field_dict)
    return field_dicts
