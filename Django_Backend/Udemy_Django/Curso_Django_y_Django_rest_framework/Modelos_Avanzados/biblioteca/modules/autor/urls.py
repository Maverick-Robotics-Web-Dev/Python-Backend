from django.urls import path

from .views import *

urlpatterns = [
    path('', ListAuthors.as_view(),name='authors'),
]