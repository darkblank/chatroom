from django.conf.urls import include, url

from django.contrib import admin

urlpatterns = [
    url(r'^chat/', include('chat.urls', namespace='chat')),
    url(r'^member/', include('member.urls', namespace='member')),
    url(r'^admin/', admin.site.urls),
]
