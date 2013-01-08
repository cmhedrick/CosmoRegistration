from consultation.models import Consult, TextResponse, Choose
from django.contrib import admin

class ChooseInline(admin.TabularInline):
    model = Choose
    extra = 2

class TextInline(admin.TabularInline):
    model = TextResponse
    extra = 1

class ConsultAdmin(admin.ModelAdmin):
    inlines = [ChooseInline, TextInline]
    

admin.site.register(Consult, ConsultAdmin)
