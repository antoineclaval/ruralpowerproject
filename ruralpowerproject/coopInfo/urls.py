from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from coopInfo import views

urlpatterns = [
    url(r'^api/persons/$', views.PersonList.as_view()),
    url(r'^web/persons/$', views.PersonListWeb.as_view()),

    url(r'^api/persons/(?P<pk>[0-9]+)/$', views.PersonDetail.as_view()),

    url(r'^api/states/$', views.StateList.as_view()),
    url(r'^api/states/(?P<pk>[0-9]+)/$', views.StateDetail.as_view()),

    url(r'^api/cooperatives/$', views.CooperativeList.as_view()),
    url(r'^web/cooperatives/$', views.CooperativeListWeb.as_view()),
    
    url(r'^api/cooperatives/(?P<pk>[0-9]+)/$', views.CooperativeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)