from django.contrib import admin

from .models import Person, Movie, Alias
from utils import *


class MovieAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'release_year',
        'display_release_year'
	)

    list_display_links = ('title',)

    list_filter = [
        'release_year',
        'casting',
        'directors',
        'producers'
    ]

    search_fields = [
        'title',
        'release_year',
    ]

    def display_release_year(self, obj):
        return int_to_roman(obj.release_year)

    display_release_year.short_description = 'Roman Release Year'

    class Meta:
        model = Movie


class PersonAdmin(admin.ModelAdmin):

    list_display = (
        'first_name',
        'last_name'
	)

    list_display_links = ('first_name', 'last_name')

    search_fields = [
		'first_name',
        'last_name'	
    ]

    class Meta:
        model = Person

admin.site.register(Person, PersonAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Alias)
