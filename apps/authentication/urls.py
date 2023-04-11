from django.urls import path
from django.contrib.auth.views import LogoutView

from apps.authentication.views import LoginPageView

app_name = 'auth'
urlpatterns = [
    path('', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
