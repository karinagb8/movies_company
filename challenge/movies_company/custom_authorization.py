from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized


class TrustedUsersOnlyCanEditAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list

    def read_detail(self, object_list, bundle):
        return True

    def create_list(self, object_list, bundle):
        try:
            if bundle.request.user.is_superuser():
                return object_list
            else:
                return False    
        except:
            return False

    def create_detail(self, object_list, bundle):
        try:
            return bundle.request.user.is_superuser()
        except:
            return False

    def update_list(self, object_list, bundle):
        try:
            if bundle.request.user.is_superuser():
                return object_list
            else:
                return False    
        except:
            return False

    def update_detail(self, object_list, bundle):
        try:
            return bundle.request.user.is_superuser()
        except:
            return False

    def delete_list(self, object_list, bundle):
        try:
            return bundle.request.user.is_superuser()
        except:
            return False

    def delete_detail(self, object_list, bundle):
        try:
            return bundle.request.user.is_superuser()
        except:
            return False
