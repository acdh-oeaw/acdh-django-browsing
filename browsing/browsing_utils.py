import django_tables2

from django.conf import settings
from django.utils.safestring import mark_safe
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django_tables2.export.views import ExportMixin


if "charts" in settings.INSTALLED_APPS:
    from charts.models import ChartConfig
    from charts.views import create_payload


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
        id = django_tables2.LinkColumn()

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
        self.helper.form_tag = False
        self.add_input(Submit("Filter", "Search"))


class GenericListView(ExportMixin, django_tables2.SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = "filter"
    paginate_by = 50
    template_name = "browsing/generic_list.html"
    init_columns = []
    enable_merge = False
    excluded_cols = []

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
        self.filter = self.filter_class(self.request.GET, queryset=qs)
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
        context["docstring"] = "{}".format(self.model.__doc__)
        if self.model._meta.verbose_name_plural:
            context["class_name"] = "{}".format(self.model._meta.verbose_name.title())
        else:
            if self.model.__name__.endswith("s"):
                context["class_name"] = "{}".format(self.model.__name__)
            else:
                context["class_name"] = "{}s".format(self.model.__name__)
        try:
            context["create_view_link"] = self.model.get_createview_url()
        except AttributeError:
            context["create_view_link"] = None
        model_name = self.model.__name__.lower()
        context["entity"] = model_name
        context["app_name"] = self.model._meta.app_label
        if "charts" in settings.INSTALLED_APPS:
            model = self.model
            app_label = model._meta.app_label
            filtered_objs = ChartConfig.objects.filter(
                model_name=model.__name__.lower(), app_name=app_label
            )
            context["vis_list"] = filtered_objs
            context["property_name"] = self.request.GET.get("property")
            context["charttype"] = self.request.GET.get("charttype")
            if context["charttype"] and context["property_name"]:
                qs = self.get_queryset()
                chartdata = create_payload(
                    context["entity"],
                    context["property_name"],
                    context["charttype"],
                    qs,
                    app_label=app_label,
                )
                context = dict(context, **chartdata)
        return context


class BaseDetailView(DetailView):
    model = None
    template_name = "browsing/generic_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["docstring"] = "{}".format(self.model.__doc__)
        context["class_name"] = "{}".format(self.model.__name__)
        context["app_name"] = "{}".format(self.model._meta.app_label)
        return context


class BaseCreateView(CreateView):
    model = None
    form_class = None
    template_name = "browsing/generic_create.html"

    def get_context_data(self, **kwargs):
        context = super(BaseCreateView, self).get_context_data()
        context["docstring"] = "{}".format(self.model.__doc__)
        context["class_name"] = "{}".format(self.model.__name__)
        return context


class BaseUpdateView(UpdateView):
    model = None
    form_class = None
    template_name = "browsing/generic_create.html"

    def get_context_data(self, **kwargs):
        context = super(BaseUpdateView, self).get_context_data()
        context["docstring"] = "{}".format(self.model.__doc__)
        context["class_name"] = "{}".format(self.model.__name__)
        # if self.model.__name__.endswith('s'):
        #     context['class_name'] = "{}".format(self.model.__name__)
        # else:
        #     context['class_name'] = "{}s".format(self.model.__name__)
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
