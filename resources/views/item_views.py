from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Item
from ..forms import ItemForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class ItemListView(ListView):
    model = Item
    template_name = "resources/item_list.html"
    paginate_by = 20
    context_object_name = "item_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(ItemListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ItemListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ItemListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ItemListView, self).get_queryset()

    def get_allow_empty(self):
        return super(ItemListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(ItemListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(ItemListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(ItemListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(ItemListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(ItemListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(ItemListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ItemListView, self).get_template_names()


class ItemDetailView(DetailView):
    model = Item
    template_name = "resources/item_detail.html"
    context_object_name = "item"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(ItemDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ItemDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ItemDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ItemDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(ItemDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(ItemDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ItemDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ItemDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ItemDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ItemDetailView, self).get_template_names()


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    fields = ['name', 'reference', 'parent_item', 'description', 'image', 'price']
    template_name = "resources/item_create.html"
    success_url = reverse_lazy("item_list")

    def __init__(self, **kwargs):
        return super(ItemCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(ItemCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ItemCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ItemCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(ItemCreateView, self).get_form_class()

    def get_form(self, form_class):
        return super(ItemCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ItemCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ItemCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(ItemCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ItemCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ItemCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(ItemCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ItemCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("item_detail", args=(self.object.pk,))


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    fields = ['name', 'reference', 'parent_item', 'description', 'image', 'price']
    template_name = "resources/item_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "item"

    def __init__(self, **kwargs):
        return super(ItemUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ItemUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ItemUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ItemUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ItemUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ItemUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(ItemUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(ItemUpdateView, self).get_form_class()

    def get_form(self, form_class):
        return super(ItemUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ItemUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ItemUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(ItemUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ItemUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ItemUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ItemUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ItemUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ItemUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("item_detail", args=(self.object.pk,))


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "resources/item_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "item"

    def __init__(self, **kwargs):
        return super(ItemDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ItemDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ItemDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ItemDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ItemDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(ItemDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(ItemDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ItemDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ItemDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ItemDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ItemDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("item_list")
