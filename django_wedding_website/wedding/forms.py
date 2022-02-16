from django import forms
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from .models import Guest

labels = {
    "first_name": _("First Name"),
    "last_name": _("Last Name"),
    "is_attending": _("Attending"),
    "meal": _("Main course"),
    "is_child": _("Child"),
    "comments": _("Comments"),
}
fields = "__all__"
exclude = ["registration"]


class RegistrationForm(forms.ModelForm):
    error_css_class = "error"

    class Meta:
        model = Guest
        exclude = exclude
        fields = fields
        labels = labels
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name..."}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name..."}),
            "comments": forms.TextInput(
                attrs={
                    "placeholder": "Anything else we should know about (Allergies,...)?"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.empty_permitted = False

    def clean(self):
        cleaned_data = super().clean()
        is_attending = cleaned_data.get("is_attending")
        meal = cleaned_data.get("meal")

        if is_attending and not meal:
            # Only do something if both fields are valid so far.
            self.add_error("meal", ValidationError("Please select a meal option."))


BaseRegistrationFormSet = forms.modelformset_factory(
    model=Guest,
    form=RegistrationForm,
    exclude=exclude,
    fields=fields,
    labels=labels,
    extra=1,
)


class RegistrationFormSet(BaseRegistrationFormSet):
    def is_valid(self):
        return super().is_valid() and all([form.is_valid() for form in self.forms])
