import random

from django.contrib.sites.models import Site
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from models import Foto, Expo, Serie

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        pool = list( Foto.objects.all() )
        random.shuffle( pool )
        context['fotos'] = pool[:5]
        context['expos'] = Expo.objects.all()

        return context

