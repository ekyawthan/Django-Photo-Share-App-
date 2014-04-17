from __future__ import unicode_literals 
from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from collections import defaultdict
from django.http import HttpResponseRedirect, HttpResponse 
from django.shortcuts import get_object_or_404, render_to_response


def home(request):
    if (request.user.is_authenticated()):
        return render(request, 'home.html')
    return login(request, template_name='home.html')

@login_required
def profile(request):
    return render(request, template_name='user_profile/profile.html')