from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    context=Video.objects.all()
    return render(request,('qoyish/home.html'),{'context':context})