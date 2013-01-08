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
