'''
Models for cattle production history records.
'''

from django.db import models

class Cow(models.Model): pass

class Cow(models.Model):
    '''The cow model for cow production history'''
    dam_breed=models.CharField(max_length=100)
    sire_breed=models.CharField(max_length=100)
    dam=models.ForeignKey(Cow,on_delete=models.CASCADE)
    sire=models.ForeignKey(Cow,on_delete=models.CASCADE)
    description=models.CharField(max_length=256)
    birth_date=models.DateTimeField()
    purchase_date=models.DateTimeField()
    weaning_weight=models.FloatField()
    purchase_price=models.FloatField()
    def __str__(self):
        return self.description



class CowSale(models.Model):
    '''The sales record of a cow'''
    cow=models.ForeignKey(Cow,on_delete=models.CASCADE)
    date_of_sale=models.DateTimeField()
    reason=models.CharField(max_length=256)
    sale_price=models.FloatField()
    sale_weight=models.FloatField()
    def __str__(self):
        return self.reason

