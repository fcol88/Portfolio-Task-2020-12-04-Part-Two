from django.shortcuts import render
from django.http import HttpResponse
from .models import Prescription

def index(request):
    return HttpResponse("This is where you'll be asked "
    "to enter drugs.")

def confirm(request):
    return HttpResponse("This is where you'll be asked "
    "to confirm your responses.")

def viewall(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'prescriptions/prescriptions.html', {
        'prescriptions': prescriptions,
    })
