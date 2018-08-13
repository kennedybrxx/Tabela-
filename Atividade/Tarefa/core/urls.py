from django.urls import path, include
from .views import index, createtable
from .apps import CoreConfig

app_name = CoreConfig.name
urlpatterns = [
    path('', index, name='index'),
    path('table/', createtable, name='table')
]
