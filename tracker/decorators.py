from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('tracker:home')
        return wrapper_func
    return decorator


def restrict_auditor(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.has_perm('add_expense'):
            return redirect('tracker:approved_expense')
        else:
            return view_func(request, *args, **kwargs)
        # if request.user.groups.filter(name="auditor").exists():
        # else:
        #     return HttpResponse("Set groups first")

    return wrapper_func
