from django.db import models

class Prescription(models.Model):
    frequency_days = models.SmallIntegerField(default=0)

class Quantity(models.Model):
    prescription = models.ForeignKey('Prescription', on_delete=models.CASCADE)
    drug = models.ForeignKey('Drug', on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)

class Drug(models.Model):
    drug_name= models.CharField(max_length=200)