from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'listing', 'email')
    list_per_page = 25
