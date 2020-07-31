from django.conf.urls import url, include
from .api import *
from tastypie.api import Api

app_name = 'movies_company'

api = Api(api_name='movies_api')
api.register(PersonResource())
api.register(MovieResource())
api.register(AliasResource())

urlpatterns = [
    url(r'^api/', include(api.urls)),
]