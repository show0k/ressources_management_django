from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Category
from ..forms import CategoryForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class CategoryListView(ListView):
    model = Category
    template_name = "resources/category_list.html"
    paginate_by = 20
    context_object_name = "category_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CategoryListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CategoryListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CategoryListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CategoryListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CategoryListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CategoryListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CategoryListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CategoryListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CategoryListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CategoryListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CategoryListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CategoryListView, self).get_template_names()


class CategoryDetailView(DetailView):
    model = Category
    template_name = "resources/category_detail.html"
    context_object_name = "category"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CategoryDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CategoryDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CategoryDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CategoryDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CategoryDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CategoryDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CategoryDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CategoryDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CategoryDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CategoryDetailView, self).get_template_names()


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    template_name = "resources/category_create.html"
    success_url = reverse_lazy("category_list")

    def __init__(self, **kwargs):
        return super(CategoryCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CategoryCreateView, self).get_form_class()

    def get_form(self, form_class):
        return super(CategoryCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CategoryCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CategoryCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CategoryCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CategoryCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CategoryCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CategoryCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CategoryCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("category_detail", args=(self.object.pk,))


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = "resources/category_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "category"

    def __init__(self, **kwargs):
        return super(CategoryUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CategoryUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CategoryUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CategoryUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CategoryUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CategoryUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CategoryUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CategoryUpdateView, self).get_form_class()

    def get_form(self, form_class):
        return super(CategoryUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CategoryUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CategoryUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CategoryUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CategoryUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CategoryUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CategoryUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CategoryUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CategoryUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("category_detail", args=(self.object.pk,))


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "resources/category_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "category"

    def __init__(self, **kwargs):
        return super(CategoryDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CategoryDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CategoryDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CategoryDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CategoryDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CategoryDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CategoryDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CategoryDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CategoryDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("category_list")
