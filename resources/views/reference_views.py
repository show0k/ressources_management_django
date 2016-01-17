from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Reference
from ..forms import ReferenceForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class ReferenceListView(ListView):
    model = Reference
    template_name = "resources/reference_list.html"
    paginate_by = 20
    context_object_name = "reference_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(ReferenceListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ReferenceListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ReferenceListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ReferenceListView, self).get_queryset()

    def get_allow_empty(self):
        return super(ReferenceListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(ReferenceListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(ReferenceListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(ReferenceListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(ReferenceListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(ReferenceListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(ReferenceListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ReferenceListView, self).get_template_names()


class ReferenceDetailView(DetailView):
    model = Reference
    template_name = "resources/reference_detail.html"
    context_object_name = "reference"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(ReferenceDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ReferenceDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ReferenceDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ReferenceDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(ReferenceDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(ReferenceDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ReferenceDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ReferenceDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ReferenceDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ReferenceDetailView, self).get_template_names()


class ReferenceCreateView(CreateView):
    model = Reference
    form_class = ReferenceForm
    fields = ['name', 'category', 'description', 'image']
    template_name = "resources/reference_create.html"
    success_url = reverse_lazy("reference_list")

    def __init__(self, **kwargs):
        return super(ReferenceCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(ReferenceCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ReferenceCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ReferenceCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(ReferenceCreateView, self).get_form_class()

    def get_form(self, form_class):
        return super(ReferenceCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ReferenceCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ReferenceCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(ReferenceCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ReferenceCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ReferenceCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(ReferenceCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ReferenceCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("reference_detail", args=(self.object.pk,))


class ReferenceUpdateView(UpdateView):
    model = Reference
    form_class = ReferenceForm
    fields = ['name', 'category', 'description', 'image']
    template_name = "resources/reference_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "reference"

    def __init__(self, **kwargs):
        return super(ReferenceUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ReferenceUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ReferenceUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ReferenceUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ReferenceUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ReferenceUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(ReferenceUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(ReferenceUpdateView, self).get_form_class()

    def get_form(self, form_class):
        return super(ReferenceUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ReferenceUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ReferenceUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(ReferenceUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ReferenceUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ReferenceUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ReferenceUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ReferenceUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ReferenceUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("reference_detail", args=(self.object.pk,))


class ReferenceDeleteView(DeleteView):
    model = Reference
    template_name = "resources/reference_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "reference"

    def __init__(self, **kwargs):
        return super(ReferenceDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ReferenceDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ReferenceDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ReferenceDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ReferenceDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(ReferenceDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(ReferenceDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ReferenceDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ReferenceDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ReferenceDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ReferenceDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("reference_list")
