from django.contrib import admin

from .models import Person, Movie, Alias

admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(Alias)
