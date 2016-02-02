from django.conf.urls import url

from . import views

app_name = 'jobs'
urlpatterns = [
    url(r'^(?P<school_id>[0-9]+)/$', views.index, name='index'),
    url(r'^(?P<school_id>[0-9]+)/(?P<job_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^user/(?P<username>[-\w]+)/$',views.user, name='user'),
    url(r'^accounts/login/$',views.login_user, name='login_user'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
    {'next_page': '/'}),
    url(r'^get_jobs/$', views.get_jobs, name='get_jobs'),
]
