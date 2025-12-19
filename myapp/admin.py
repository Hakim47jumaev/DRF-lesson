from django.contrib import admin
from .models import Book,Author,Course,Car


admin.site.register([Book,Author,Course])

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display=['model','brend','owner']
    list_filter=['model','brend','owner']
    search_fields=['model','brend','owner']