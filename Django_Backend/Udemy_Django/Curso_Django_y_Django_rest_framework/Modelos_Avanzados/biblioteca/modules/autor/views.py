from django.shortcuts import render
from django.views.generic import ListView

from .models import *

# Create your views here.


class ListAuthors(ListView):
    context_object_name = 'list_authors'
    template_name = 'author/list.html'

    def get_queryset(self):
        return Author.objects.list_authors()