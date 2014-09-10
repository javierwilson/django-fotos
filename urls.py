from django.views.generic import TemplateView, ListView, DetailView
from django.conf.urls import patterns, url
from models import Expo, Serie, Foto
from views import IndexView

urlpatterns = patterns('fotos.views',
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^expo/$', ListView.as_view(model=Expo), name='expo_list'),
    url(r'^expo/(?P<pk>\d+)/$', DetailView.as_view(model=Expo), name='expo_detail'),
    url(r'^serie/$', ListView.as_view(model=Serie), name='serie_list'),
    url(r'^serie/(?P<pk>\d+)/$', DetailView.as_view(model=Serie), name='serie_detail'),
    url(r'^foto/$', ListView.as_view(model=Foto), name='foto_list'),
    url(r'^foto/(?P<pk>\d+)/$', DetailView.as_view(model=Foto), name='foto_detail'),
    url(r'^foto/(?P<slug>[-\w\d]+)/$', DetailView.as_view(), name='foto_detail'),
)
