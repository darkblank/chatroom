from django.conf.urls import url

from member.views import signup, log_out

app_name = 'member'

urlpatterns = [
    url(r'^$', signup, name='signup'),
    url(r'^logout/$', log_out, name='log_out')
]
