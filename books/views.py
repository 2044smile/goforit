from django.shortcuts import render
from django.http import HttpResponse

from .models import Books


def index(request):
    target = Books.objects.all()

    context = {
        'keys': target
    }

    return render(request, 'books/index.html', context)
