from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/mock/admin/', admin.site.urls),
    path('api/mock/mockapp/', include('mockapp.urls')),
]
