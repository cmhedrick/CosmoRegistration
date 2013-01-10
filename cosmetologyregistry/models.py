import datetime
from django.utils import timezone
from django.db import models

class Consult(models.Model):
    question = models.CharField(max_length=200)
    def __unicode__(self):
        return self.question

class TextResponse(models.Model):
    consult = models.ForeignKey(Consult)
    text = models.CharField(max_length=500)
    def __unicode__(self):
        return self.text

class Choose(models.Model):
    consult = models.ForeignKey(Consult)
    choose = models.CharField(max_length=200)
    def __unicode__(self):
        return self.choose

SERVICE_IDS = (
    ("HS", 'Hairshaping'),
    ("SS", 'Shampoo & Style'),
    ("WS", 'Wig Services'),
    ("BT", 'Bleaching & Tinting'),
    ("ST", 'Hair And Scalp Treatment'),
    ("NS", 'Nail Services'),
    ("CR", 'Color Rinse'),
    ("CH", 'Chemical Hair Relaxers'),
    ("PM", 'Permanents'),
    ("FT", 'Facial Treatments'),
    ("WT", 'Waxing Treatments'),
)   

class Service(models.Model):
    service_ids = models.CharField(max_length=2, choices=SERVICE_IDS)
    hairservice = models.CharField(max_length=200)
    student_prices = models.DecimalField(max_digits=19, decimal_places=10)
    prices = models.DecimalField(max_digits=19, decimal_places=10)
    as_of = models.DateTimeField('date published')
    def __unicode__(self):
        return self.hairsevice

