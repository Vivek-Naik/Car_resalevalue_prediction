from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render
from sell.models import Selll

def buy(request):
    cars = Selll.objects.all()
    return render(request, 'buy/car_details.html', {'cars': cars})
