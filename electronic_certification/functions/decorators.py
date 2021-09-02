from django.shortcuts import redirect
from django.urls import reverse


def login_required(view_func):
    def wrapper(request, *view_args, **view_kwargs):
        if request.session.has_key('islogin'):
            return view_func(request, *view_args, **view_kwargs)
        else:
            return redirect(reverse('myapp:login'))

    return wrapper
