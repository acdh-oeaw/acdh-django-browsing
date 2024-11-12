from django.contrib import admin

from archiv.models import Person, Place, Book

admin.site.register(Person)
admin.site.register(Place)
admin.site.register(Book)