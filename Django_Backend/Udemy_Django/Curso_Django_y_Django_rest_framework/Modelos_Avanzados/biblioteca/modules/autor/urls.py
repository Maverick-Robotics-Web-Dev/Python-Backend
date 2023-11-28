from django.urls import path

from .views import *

urlpatterns = [
    path('authors/', ListAuthors.as_view(),name='authors'),
]