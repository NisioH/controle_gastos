from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    now = datetime.datetime.now()

    return render(request, 'contas/home.html')
