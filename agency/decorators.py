from django.http import HttpResponse
from django.shortcuts import redirect

def is_agency(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_agency:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized to this page')
    return wrapper_func