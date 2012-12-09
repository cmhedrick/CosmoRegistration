import datetime
from django.utils import timezone
from django.db import models

SERVICE_IDS = (
    ("HS", 'Hairshaping'),
    ("SS", 'Shampoo & Style'),
    ("WS", 'Wigs'),
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
    studentprices = models.DecimalField(max_digits=19, decimal_places=10)
    prices = models.DecimalField(max_digits=19, decimal_places=10)
    as_of = models.DateTimeField('date published')
    def __unicode__(self):
        return self.hairsevice
