from django.urls import path
from .views import handle_get_request

urlpatterns = [
    path('get/', handle_get_request, name='handle_get_request'),
]
