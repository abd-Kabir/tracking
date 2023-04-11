from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.dashboard.views import TrackListView, TrackCreateView, TrackUpdateDetailView, TrackCreatePageView, \
    TrackUpdateView, TrackDeleteView

app_name = 'dashboard'
urlpatterns = [
    path('', login_required(TrackListView.as_view()), name='list'),
    path('create/', login_required(TrackCreateView.as_view()), name='create'),
    path('update/<int:pk>/', login_required(TrackUpdateView.as_view()), name='update'),
    path('delete/<int:pk>/', login_required(TrackDeleteView.as_view()), name='delete'),
    path('update-page/<int:pk>/', login_required(TrackUpdateDetailView.as_view()), name='update-page'),
    path('create-page/', login_required(TrackCreatePageView.as_view()), name='create-page'),
]
