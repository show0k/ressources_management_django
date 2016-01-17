from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import State
from ..forms import StateForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class StateListView(ListView):
    model = State
    template_name = "resources/state_list.html"
    paginate_by = 20
    context_object_name = "state_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(StateListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StateListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StateListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(StateListView, self).get_queryset()

    def get_allow_empty(self):
        return super(StateListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(StateListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(StateListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(StateListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(StateListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(StateListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(StateListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StateListView, self).get_template_names()


class StateDetailView(DetailView):
    model = State
    template_name = "resources/state_detail.html"
    context_object_name = "state"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(StateDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StateDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StateDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StateDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(StateDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(StateDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(StateDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StateDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StateDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StateDetailView, self).get_template_names()


class StateCreateView(CreateView):
    model = State
    form_class = StateForm
    fields = ['creator', 'is_active', 'creation_date', 'last_modification_date', 'passived_date', 'description', 'working_state']
    template_name = "resources/state_create.html"
    success_url = reverse_lazy("state_list")

    def __init__(self, **kwargs):
        return super(StateCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(StateCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StateCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(StateCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(StateCreateView, self).get_form_class()

    def get_form(self, form_class):
        return super(StateCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(StateCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(StateCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(StateCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(StateCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(StateCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(StateCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StateCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("state_detail", args=(self.object.pk,))


class StateUpdateView(UpdateView):
    model = State
    form_class = StateForm
    fields = ['creator', 'is_active', 'creation_date', 'last_modification_date', 'passived_date', 'description', 'working_state']
    template_name = "resources/state_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "state"

    def __init__(self, **kwargs):
        return super(StateUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StateUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StateUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(StateUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StateUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(StateUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(StateUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(StateUpdateView, self).get_form_class()

    def get_form(self, form_class):
        return super(StateUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(StateUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(StateUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(StateUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(StateUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(StateUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StateUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StateUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StateUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("state_detail", args=(self.object.pk,))


class StateDeleteView(DeleteView):
    model = State
    template_name = "resources/state_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "state"

    def __init__(self, **kwargs):
        return super(StateDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StateDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(StateDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(StateDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StateDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(StateDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(StateDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(StateDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StateDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StateDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StateDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("state_list")
