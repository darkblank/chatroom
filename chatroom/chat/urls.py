from django.conf.urls import url

from chat.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]
