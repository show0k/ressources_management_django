from django import forms
from .models import Category, Item, State, Loan, Reference


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'description']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CategoryForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CategoryForm, self).is_valid()

    def full_clean(self):
        return super(CategoryForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean(self):
        return super(CategoryForm, self).clean()

    def validate_unique(self):
        return super(CategoryForm, self).validate_unique()

    def save(self, commit=True):
        return super(CategoryForm, self).save(commit)


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'reference', 'parent_item', 'description', 'image', 'price']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(ItemForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(ItemForm, self).is_valid()

    def full_clean(self):
        return super(ItemForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_reference(self):
        reference = self.cleaned_data.get("reference", None)
        return reference

    def clean_parent_item(self):
        parent_item = self.cleaned_data.get("parent_item", None)
        return parent_item

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_image(self):
        image = self.cleaned_data.get("image", None)
        return image

    def clean_price(self):
        price = self.cleaned_data.get("price", None)
        return price

    def clean(self):
        return super(ItemForm, self).clean()

    def validate_unique(self):
        return super(ItemForm, self).validate_unique()

    def save(self, commit=True):
        return super(ItemForm, self).save(commit)


class StateForm(forms.ModelForm):

    class Meta:
        model = State
        fields = ['creator', 'is_active', 'creation_date', 'last_modification_date', 'passived_date', 'description', 'working_state']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(StateForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(StateForm, self).is_valid()

    def full_clean(self):
        return super(StateForm, self).full_clean()

    def clean_creator(self):
        creator = self.cleaned_data.get("creator", None)
        return creator

    def clean_is_active(self):
        is_active = self.cleaned_data.get("is_active", None)
        return is_active

    def clean_creation_date(self):
        creation_date = self.cleaned_data.get("creation_date", None)
        return creation_date

    def clean_last_modification_date(self):
        last_modification_date = self.cleaned_data.get("last_modification_date", None)
        return last_modification_date

    def clean_passived_date(self):
        passived_date = self.cleaned_data.get("passived_date", None)
        return passived_date

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_working_state(self):
        working_state = self.cleaned_data.get("working_state", None)
        return working_state

    def clean(self):
        return super(StateForm, self).clean()

    def validate_unique(self):
        return super(StateForm, self).validate_unique()

    def save(self, commit=True):
        return super(StateForm, self).save(commit)


class LoanForm(forms.ModelForm):

    class Meta:
        model = Loan
        fields = ['creator', 'is_active', 'creation_date', 'last_modification_date', 'passived_date', 'description', 'priority', 'renter', 'starting_date', 'ending_date']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(LoanForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(LoanForm, self).is_valid()

    def full_clean(self):
        return super(LoanForm, self).full_clean()

    def clean_creator(self):
        creator = self.cleaned_data.get("creator", None)
        return creator

    def clean_is_active(self):
        is_active = self.cleaned_data.get("is_active", None)
        return is_active

    def clean_creation_date(self):
        creation_date = self.cleaned_data.get("creation_date", None)
        return creation_date

    def clean_last_modification_date(self):
        last_modification_date = self.cleaned_data.get("last_modification_date", None)
        return last_modification_date

    def clean_passived_date(self):
        passived_date = self.cleaned_data.get("passived_date", None)
        return passived_date

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_priority(self):
        priority = self.cleaned_data.get("priority", None)
        return priority

    def clean_renter(self):
        renter = self.cleaned_data.get("renter", None)
        return renter

    def clean_starting_date(self):
        starting_date = self.cleaned_data.get("starting_date", None)
        return starting_date

    def clean_ending_date(self):
        ending_date = self.cleaned_data.get("ending_date", None)
        return ending_date

    def clean(self):
        return super(LoanForm, self).clean()

    def validate_unique(self):
        return super(LoanForm, self).validate_unique()

    def save(self, commit=True):
        return super(LoanForm, self).save(commit)


class ReferenceForm(forms.ModelForm):

    class Meta:
        model = Reference
        fields = ['name', 'category', 'description', 'image']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(ReferenceForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(ReferenceForm, self).is_valid()

    def full_clean(self):
        return super(ReferenceForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_category(self):
        category = self.cleaned_data.get("category", None)
        return category

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_image(self):
        image = self.cleaned_data.get("image", None)
        return image

    def clean(self):
        return super(ReferenceForm, self).clean()

    def validate_unique(self):
        return super(ReferenceForm, self).validate_unique()

    def save(self, commit=True):
        return super(ReferenceForm, self).save(commit)
