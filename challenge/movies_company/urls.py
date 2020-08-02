from django.conf.urls import url, include
from .api import *
from tastypie.api import Api


api = Api(api_name='api')
api.register(PersonResource())
api.register(MovieResource())
api.register(AliasResource())

urlpatterns = [
    url('', include(api.urls)),
]