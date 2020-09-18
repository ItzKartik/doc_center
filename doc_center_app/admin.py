from django.contrib import admin
from doc_center_app import models

admin.site.register(models.types)

class bids_admin(admin.TabularInline):
    model = models.bids

@admin.register(models.docs)
class first_admin(admin.ModelAdmin):
    inlines = [
        bids_admin
    ]