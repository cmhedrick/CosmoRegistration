from django.db import models

class Head(models.Model):
    question = models.CharField(max_length=200)
    def __unicode__(self):
        return self.question

class TextResponse(models.Model):
    head = models.ForeignKey(Head)
    text = models.CharField(max_length=500)
    def __unicode__(self):
        return self.text

class Choose(models.Model):
    head = models.ForeignKey(Head)
    choose = models.CharField(max_length=200)
    def __unicode__(self):
        return self.choose 
