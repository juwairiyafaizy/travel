from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


def demo(request):
    obj = Place.objects.all()
    teams = Team.objects.all()
    return render(request, "index.html",{'result':obj , 'persons':teams})
