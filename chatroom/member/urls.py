from django.conf.urls import url

from member.views import signup

app_name = 'member'

urlpatterns = [
    url(r'^$', signup, name='signup'),
]
