from django.contrib import admin
from .models import Prescription, Quantity, Drug

admin.site.register(Prescription)
admin.site.register(Quantity)
admin.site.register(Drug)

