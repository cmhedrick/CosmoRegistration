import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

GENDER = (
    ("Male", 'Male'),
    ("Female", 'Female'),
)   

SKIN_TYPE = (
    ("Dry", 'Dry'),
    ("Oily", 'Oily'),
    ("Normal", 'Combination'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(blank=True, max_length=13)
    gender = models.CharField(blank=True, max_length=4, choices=GENDER)
    age = models.IntegerField(blank=True, null=True)
    heard_from = models.CharField(blank=True, max_length=300)
    referrer = models.CharField(blank=True, max_length=200)
    last_visit = models.DateTimeField(blank=True, null=True)
    meds = models.CharField(blank=True, max_length=300)
    natural_hair_color = models.CharField(blank=True, max_length=300)
    hair_condition = models.CharField(blank=True, max_length=300)
    hair_texture = models.CharField(blank=True, max_length=200)
    scalp_condition = models.CharField(blank=True, max_length=300)
    skin_type = models.CharField(blank=True, max_length=4, choices=SKIN_TYPE)

class Appointment(models.Model):
    user = models.ForeignKey(User)
    date_time = models.DateTimeField()
    
    def __unicode__(self):
        return "%s %s" % (self.user, self.date_time)

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

