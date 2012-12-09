from consultation.models import Head, TextResponse, Choose
from django.contrib import admin

class ChooseInline(admin.TabularInline):
    model = Choose
    extra = 2

class TextInline(admin.TabularInline):
    model = TextResponse
    extra = 1

class HeadAdmin(admin.ModelAdmin):
    inlines = [ChooseInline, TextInline]
    

admin.site.register(Head, HeadAdmin)
