from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView

from .models import Author, Book


class AuthorCreateView(CreateView):
    model = Author
    fields = '__all__'


def index(request):
    return render(request, 'index.html')