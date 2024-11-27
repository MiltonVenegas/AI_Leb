from django.urls import path, include
from MainApp.views import *
from django.conf import settings
from conf.urls.static import static

urlpatterns = [
    path('', Inicio.as_view(), name='index')
]