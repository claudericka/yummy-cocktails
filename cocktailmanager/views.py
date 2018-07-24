
from django.shortcuts import render
from cocktailmanager.utils.populate import populate as populate_db
from django.http import HttpResponse


def index(request):
    return render(request, 'cocktailmanager/index.html')


def populate(request):
    populate_db()
    return HttpResponse("Populate success")