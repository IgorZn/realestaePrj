from django.contrib import admin

from .models import Listing, Realtor


@admin.register(Listing)
class AdminListing(admin.ModelAdmin):
    pass


@admin.register(Realtor)
class AdminRealtor(admin.ModelAdmin):
    pass
