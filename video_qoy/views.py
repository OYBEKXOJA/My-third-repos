from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    index=Qoyish.objects.all()
    return render(request,('video_qoy/home.html'),{'index':index})