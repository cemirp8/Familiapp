from django.contrib import admin
from django.urls import path
from Familiapp.views import familiares


urlpatterns = [
    path('admin/', admin.site.urls),
    path('familiares/', familiares)   
]