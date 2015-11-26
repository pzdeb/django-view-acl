from django.contrib.auth.models import Permission
from django.http import HttpResponseForbidden

#MOCK for generate_func_perm(in future will be replaced by real func)
def generate_func_perm(func_name):
    return 'Can add log entry'

class CustomViewProcessMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):
        user = request.user
        if user.is_authenticated():
            func_perm = generate_func_perm(view_func)
            perm = Permission.objects.filter(name=func_perm)

            #Permition doesn't exist in db(view is allowed)
            if not perm:
                return view_func(request, *view_args, **view_kwargs)

            #User doesn't have permission to called view
            if not user.has_perm(perm):
                return HttpResponseForbidden()

        #Anonymous user doesn't have any restrictions
        return view_func(request, *view_args, **view_kwargs)