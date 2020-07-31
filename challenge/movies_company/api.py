from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from .models import *
from utils import *


class AliasResource(ModelResource):
    class Meta:
        queryset = Alias.objects.all()
        resource_name = 'aliases'


class PersonResource(ModelResource):
    aliases = fields.ToManyField(AliasResource, 'aliases', full=True, full_detail=True)
    movies_as_actor_actress = fields.ToManyField('movies_company.api.MovieResource', 'movies_as_actor_actress', full=True, full_detail=True)
    movies_as_director = fields.ToManyField('movies_company.api.MovieResource', 'movies_as_director', full=True, full_detail=True)
    movies_as_producer = fields.ToManyField('movies_company.api.MovieResource', 'movies_as_producer', full=True, full_detail=True)

    class Meta:
        queryset = Person.objects.all()
        resource_name = 'persons'


class MovieResource(ModelResource):
    casting = fields.ToManyField(PersonResource, 'casting', full=True, full_detail=False)
    directors = fields.ToManyField(PersonResource, 'directors', full=True, full_detail=False)
    producers = fields.ToManyField(PersonResource, 'producers', full=True, full_detail=False)
    release_year = fields.CharField()

    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'

    def dehydrate_release_year(self, bundle):
        return int_to_roman(bundle.obj.release_year)
