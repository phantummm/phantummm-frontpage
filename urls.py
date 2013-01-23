from django.conf.urls import patterns, url

from frontpage import views

urlpatterns = patterns('frontpage.views',
    url(r'^$', 'project_list'),
    url(r'^(?P<slug>[^\.]+)/$', 'project', name='project_page'),
)
