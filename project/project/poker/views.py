from django.shortcuts import render
from django.http import HttpResponse
#from migrations.poker_headsup_main import test

# Create your views here.
def top_page(request):
    return render(request,'poker/main.html')

