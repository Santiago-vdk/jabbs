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
import json

from jobs.forms import *
from django.views.decorators.csrf import csrf_protect

from django.utils import timezone

from endless_pagination.decorators import page_template

from .models import Job, Company, School, InvitationCode


def root(request):
    current_user = request.user
    school_list = School.objects.all()    

    context = {'school_list':school_list,
               'current_user':current_user}
    
    return render(request, 'jobs/welcome.html', context)    



@login_required(login_url='/jobs/accounts/login/')
def index(request, school_id):
    current_user = request.user

    current_school = get_object_or_404(School, pk=school_id)
    job_list = Job.objects.all().filter(school = current_school)

    latest_job_list = []

    #Trabajos que han expirado
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
               'school':current_school,
               'current_user':current_user}
    
    return render(request, 'jobs/index.html', context)



@login_required(login_url='/jobs/accounts/login/')
def detail(request, school_id, job_id):
    current_user = request.user

    #Initial validations
    current_school = get_object_or_404(School, pk=school_id)
    current_job = get_object_or_404(Job, pk=job_id)

    try:
        job = Job.objects.all().filter(school = current_school).get(pk=job_id)
    
        today = datetime.now()
        days_left = str(job.exp_date.date() - today.date() )    
        days_left = days_left[:days_left.find(',')]
        return render(request, 'jobs/detail.html', {'job': job,
                                                    'school':current_school,
                                                    'days_left':days_left,
                                                    'current_user':current_user})
    except Job.DoesNotExist:
        raise Http404("Job does not exist in this school")

def user(request, username):
    user = get_object_or_404(User, username=username)
    context = {'owner': user}
    return render(request, 'jobs/user_profile.html', context)

@csrf_protect
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
       
            current_code = form.cleaned_data['invite_code']
            try:
                code = InvitationCode.objects.all().filter(code = current_code).get()
                if code.is_used != True:
                    user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'],
                    email=form.cleaned_data['email'])
                    
                    code.user = user
                    code.is_used = True
                    code.used_date = timezone.now()

                    code.save()
                else:
                    raise Http404("Invitation Code is used")  

                
                return HttpResponseRedirect('success/')
            
            except InvitationCode.DoesNotExist:
                raise Http404("Invitation Code does not exist")                    
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'jobs/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'jobs/success.html',
    )

def login_user(request):
    if (request.user.is_authenticated() == False):
        username = password = ''
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            next = request.POST.get('next')

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    
                    if next is not None:
                        return redirect(next)
                    else:
                        return HttpResponseRedirect('/')

        return render(request,'jobs/login.html')         
    else:
        return HttpResponseRedirect('/')        
        
def logout_user(request):
    if (request.user.is_authenticated()):    
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')        


@login_required(login_url='/jobs/accounts/login/')
def get_jobs(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        jobs = Job.objects.filter(name__icontains = q )[:20]
        results = []
        for job in jobs:
            job_json = {}
            job_json = job.id
            job_json = job.school
            job_json = job.name
            results.append(job_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
