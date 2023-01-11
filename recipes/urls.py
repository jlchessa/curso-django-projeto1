# from django.http import HttpResponse
from django.urls import path

from recipes.views import about, contact, home

urlpatterns = [
    path('', home),
    path('contato/', contact),
    path('sobre/', about)
]
