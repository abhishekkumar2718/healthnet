from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^', include(('healthnet.urls', 'healthnet'), namespace="healthnet")),
    url(r'^admin/', admin.site.urls),
]
