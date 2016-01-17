from django.contrib import admin
from .models import Category, Item, State, Loan, Reference
from django_baker.admin import ExtendedModelAdminMixin


class CategoryAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = []


class ItemAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = []


class StateAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = []


class LoanAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = []


class ReferenceAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = []


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(Reference, ReferenceAdmin)
