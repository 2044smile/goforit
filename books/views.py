from django.shortcuts import render
from django.http import HttpResponse

from .models import Books


def index(request):
    Books.objects.create(title="test")
    return HttpResponse("Hello, I am human")
