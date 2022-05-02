'''
Models for cattle production history records.
'''

from django.db import models

class Cattle(models.Model): pass

class Cattle(models.Model):
    '''The cattle model for cattle production history'''
    dam_breed=models.CharField(max_length=100)
    sire_breed=models.CharField(max_length=100)
    dam=models.ForeignKey(Cattle,on_delete=models.CASCADE)
    sire=models.ForeignKey(Cattle,on_delete=models.CASCADE)
    description=models.CharField(max_length=256)
    birth_date=models.DateTimeField()
    purchase_date=models.DateTimeField()
    weaning_weight=models.FloatField()
    purchase_price=models.FloatField()
    def __str__(self):
        return self.description



class CattleSale(models.Model):
    '''The sales record of cattle'''
    cow=models.ForeignKey(Cattle,on_delete=models.CASCADE)
    date_of_sale=models.DateTimeField()
    reason=models.CharField(max_length=256)
    sale_price=models.FloatField()
    sale_weight=models.FloatField()
    def __str__(self):
        return self.reason

