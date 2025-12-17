from django.contrib import admin
from .models import Book,Author,Course


admin.site.register([Book,Author,Course])

