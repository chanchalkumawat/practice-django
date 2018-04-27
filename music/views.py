from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is the Music app homepage in branch1 ----- abcd.</h1>")

def detail(request, album_id):
    return HttpResponse("<h2>Details for album ID : %s.</h2>" % album_id)
