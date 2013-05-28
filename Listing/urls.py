from django.conf.urls import patterns, url

from Listing import views

urlpatterns = patterns('',
    url(r'^$', views.index)
)