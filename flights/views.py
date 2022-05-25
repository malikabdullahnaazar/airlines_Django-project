from django.shortcuts import render
from .models import flight,passanger
# Create your views here.
def index(request):
    return render(request,"flight/index.html",{
        "flights":flight.objects.all()
    })
def flightid(request,flightid):
    result=flight.objects.get(id=flightid)
    return render(request,"flight/flightid.html",{
        "flight_id":result,
        "passanger":flight.passangers.all()
    })