from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<city>[\w-]+)/$', views.index),
]