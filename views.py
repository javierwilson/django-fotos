from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from models import Foto, Expo, Serie

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['expos'] = Expo.objects.all()
        print context['expos']
        return context

