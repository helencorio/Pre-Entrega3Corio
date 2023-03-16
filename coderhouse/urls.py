from django.urls import path
from coderhouse.views import inicio, index

urlpatterns = [
    path('', inicio),
    path('index/', index)
]