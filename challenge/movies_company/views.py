import urllib.parse

from django.http import HttpResponse
import simplejson
from movies_company.models import *
from .serializers import *
from django.core import serializers

# # =============================================================================================
# def movies(request):
#     movies_list = Movie.objects.all()
#     return HttpResponse(
#         serializers.serialize('json', movies_list),
#         content_type="application/json"
#     )

# # =============================================================================================
# def persons(request):
#     persons_list = Person.objects.all()
#     return HttpResponse(
#         serializers.serialize('json', persons_list),
#         content_type="application/json"
#     )

# # =============================================================================================
# def alias(request):
#     alias_list = Alias.objects.all()
#     return HttpResponse(
#         serializers.serialize('json', alias_list),
#         content_type="application/json"
#     )







