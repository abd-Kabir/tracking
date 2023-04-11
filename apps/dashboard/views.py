from django.db.models import Sum, Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, TemplateView, DeleteView

from apps.dashboard.models import Track
from datetime import datetime


class TrackListView(ListView):
    model = Track
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        page_number = self.request.GET.get('page', 1)
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        tracks_count = Track.objects.all().count()
        price = Track.objects.aggregate(price=Sum('price')).get('price')
        client_price = Track.objects.aggregate(client_price=Sum('client_price')).get('client_price')
        extra_expense = Track.objects.aggregate(extra_expense=Sum('extra_expense')).get('extra_expense')

        search_query = self.request.GET.get('global-search')
        if search_query:
            tracks = Track.objects.filter(
                Q(order_num__icontains=search_query) |
                Q(box__icontains=search_query) |
                Q(container__icontains=search_query) |
                Q(shipper__icontains=search_query) |
                Q(cargo__icontains=search_query) |
                Q(customer__icontains=search_query) |
                Q(dispatch__icontains=search_query) |
                Q(load_date__icontains=search_query) |
                Q(agent__icontains=search_query) |
                Q(location__icontains=search_query) |
                Q(consignee__icontains=search_query) |
                Q(status__icontains=search_query)).order_by('-id')
        else:
            tracks = self.model.objects.all().order_by('-id')
        # paginator = Paginator(tracks, 10)
        # page_obj = paginator.get_page(page_number)
        # context['tracks'] = page_obj
        context['tracks'] = tracks
        context['totals'] = {
            'tracks_count': tracks_count,
            'price': price,
            'client_price': client_price,
            'extra_expense': extra_expense
        }
        return context


class TrackCreateView(CreateView):
    model = Track
    fields = ['order_num', 'box', 'container', 'shipper', 'cargo', 'customer', 'dispatch', 'load_date', 'agent',
              'location', 'consignee', 'price', 'client_price', 'extra_expense', 'status', ]
    success_url = reverse_lazy('dashboard:list')

    def form_valid(self, form):
        form.instance.created_at = datetime.now()
        form.instance.updated_at = datetime.now()
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.first().name == 'office_manager':
            return redirect('dashboard:list')
        return super().dispatch(request, *args, **kwargs)


class TrackUpdateView(UpdateView):
    model = Track
    fields = ['order_num', 'box', 'container', 'shipper', 'cargo', 'customer', 'dispatch', 'load_date', 'agent',
              'location', 'consignee', 'price', 'client_price', 'extra_expense', 'status', ]
    success_url = reverse_lazy('dashboard:list')

    def form_valid(self, form):
        form.instance.updated_at = datetime.now()
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.groups.first().name == 'office_manager':
    #         return redirect('dashboard:list')
    #     return super().dispatch(request, *args, **kwargs)


class TrackDeleteView(DeleteView):
    model = Track
    success_url = reverse_lazy('dashboard:list')


class TrackUpdateDetailView(DetailView):
    model = Track
    template_name = 'retrieve-update.html'


class TrackCreatePageView(TemplateView):
    template_name = 'retrieve-create.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.first().name == 'office_manager':
            return redirect('dashboard:list')
        return super().dispatch(request, *args, **kwargs)
