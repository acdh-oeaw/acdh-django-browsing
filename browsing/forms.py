from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


def get_generic_form(model_class):

    class GenericForm(forms.ModelForm):

        class Meta:
            model = model_class
            fields = "__all__"

        def __init__(self, *args, **kwargs):
            super(GenericForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_tag = True
            self.helper.form_class = "form-horizontal"
            self.helper.label_class = "col-md-3"
            self.helper.field_class = "col-md-9"
            self.helper.add_input(
                Submit("submit", "save"),
            )

    return GenericForm
