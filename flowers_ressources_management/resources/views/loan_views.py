from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Loan
from ..forms import LoanForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class LoanListView(ListView):
    model = Loan
    template_name = "resources/loan_list.html"
    paginate_by = 20
    context_object_name = "loan_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(LoanListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LoanListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LoanListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(LoanListView, self).get_queryset()

    def get_allow_empty(self):
        return super(LoanListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(LoanListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(LoanListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(LoanListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(LoanListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(LoanListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(LoanListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LoanListView, self).get_template_names()


class LoanDetailView(DetailView):
    model = Loan
    template_name = "resources/loan_detail.html"
    context_object_name = "loan"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(LoanDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LoanDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LoanDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LoanDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(LoanDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(LoanDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(LoanDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LoanDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LoanDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LoanDetailView, self).get_template_names()


class LoanCreateView(CreateView):
    model = Loan
    form_class = LoanForm
    # fields = ['renter', 'description', 'priority', 'starting_date', 'ending_date']
    template_name = "resources/loan_create.html"
    success_url = reverse_lazy("loan_list")

    def __init__(self, **kwargs):
        return super(LoanCreateView, self).__init__(**kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super(LoanCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(LoanCreateView, self).get_context_data(**kwargs)
        return ret

    def get_success_url(self):
        return reverse("loan_detail", args=(self.object.pk,))


class LoanUpdateView(UpdateView):
    model = Loan
    fields = ['creator', 'is_active', 'creation_date', 'last_modification_date', 'passived_date', 'description', 'priority', 'renter', 'starting_date', 'ending_date']
    template_name = "resources/loan_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "loan"

    def __init__(self, **kwargs):
        return super(LoanUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LoanUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LoanUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(LoanUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LoanUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(LoanUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(LoanUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(LoanUpdateView, self).get_form_class()

    def get_form(self, form_class):
        return super(LoanUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(LoanUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(LoanUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(LoanUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(LoanUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(LoanUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LoanUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LoanUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LoanUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("loan_detail", args=(self.object.pk,))


class LoanDeleteView(DeleteView):
    model = Loan
    template_name = "resources/loan_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "loan"

    def __init__(self, **kwargs):
        return super(LoanDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LoanDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(LoanDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(LoanDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LoanDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(LoanDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(LoanDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(LoanDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LoanDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LoanDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LoanDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("loan_list")
