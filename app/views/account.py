from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')