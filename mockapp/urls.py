from django.urls import path
from .views import handle_get_request,search,searchButton,list

urlpatterns = [
    path('get/', handle_get_request, name='handle_get_request'),
    path('search/', search, name='search'),
    path('list/', list, name='list'),
    path('submitsearch/', searchButton, name='submitsearch'),

]
