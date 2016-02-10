from django.conf.urls import url
from django.contrib.auth import logout

from . import views

app_name = 'jobs'
urlpatterns = [
    url(r'^(?P<school_id>[0-9]+)/$', views.index, name='index'),
    url(r'^(?P<school_id>[0-9]+)/(?P<job_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^user/(?P<username>[-\w]+)/$',views.user, name='user'),
    url(r'^accounts/register/$',views.register_user, name='register_user'),
    url(r'^accounts/register/success/$',views.register_success, name='register_success'),
    url(r'^accounts/login/$',views.login_user, name='login_user'),
    url(r'^accounts/logout/$',views.logout_user, name='logout_user'),
    url(r'^get_jobs/$', views.get_jobs, name='get_jobs'),
]
