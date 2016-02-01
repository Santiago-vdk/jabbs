from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User

from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from datetime import datetime

from .models import Job, Company




def index(request):
    current_user = request.user
    job_list = Job.objects.order_by('-pub_date')[:5]
    latest_job_list = []
    expired_job_list = []
    for i in job_list:
        today = datetime.now()
        #Valida si ya expiro la fecha de la publicacion
        if(i.exp_date.date() < today.date()):
            expired_job_list.append(i)
        else:
            latest_job_list.append(i)

    job_list = latest_job_list
            
    context = {'job_list':job_list,
               #'latest_job_list': latest_job_list,
               #'expired_job_list':expired_job_list,
               'current_user':current_user}
    return render(request, 'jobs/index.html', context)

@login_required(login_url='/jobs/accounts/login/')
def detail(request, job_id):
    current_user = request.user
    job = get_object_or_404(Job, pk=job_id)
    today = datetime.now()

    days_left = job.exp_date.date() - today.date()     
 
    return render(request, 'jobs/detail.html', {'job': job,
                                                'days_left':days_left,
                                                'current_user':current_user})

def user(request, username):
    user = get_object_or_404(User, username=username)
    context = {'owner': user}
    return render(request, 'jobs/user_profile.html', context)

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/jobs/')
    return render_to_response('jobs/login.html', context_instance=RequestContext(request))


