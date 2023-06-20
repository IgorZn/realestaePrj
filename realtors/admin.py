from django.contrib import admin
from .models import Realtor


@admin.register(Realtor)
class AdminRealtor(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name',)
    list_per_page = 25
