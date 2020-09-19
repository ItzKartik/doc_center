from django.contrib import admin
from doc_center_app import models

admin.site.register(models.types)
admin.site.register(models.type_of_membership)

class bids_admin(admin.TabularInline):
    model = models.bids

@admin.register(models.docs)
class first_admin(admin.ModelAdmin):
    inlines = [
        bids_admin
    ]