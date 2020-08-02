from tastypie.authentication import ApiKeyAuthentication
from tastypie.exceptions import Unauthorized


class NotForReadingApiKeyAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
    	try:
	    	request_method = request.META.get('REQUEST_METHOD', '')
	    	if request_method == 'GET':
	    		return True
	    	else:
	    		return super(NotForReadingApiKeyAuthentication, self).is_authenticated(request, **kwargs)
    	except:	
	    	return False
