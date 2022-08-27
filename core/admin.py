from django.contrib import admin

from .models import *

class AdminQuestion(admin.ModelAdmin):
    list_display = ['description', 'options']

admin.site.register(Question, AdminQuestion)

