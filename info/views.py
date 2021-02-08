from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import InfoSerializer
from .serializers import PhysicianSerializer
from rest_framework import generics
from django.views.generic.base import TemplateView
import requests
from datetime import date

class InfoListCreate(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class PhysiciansListCreate(generics.ListCreateAPIView):
    queryset = Physicians.objects.all()
    serializer_class = PhysicianSerializer


class IndexView(TemplateView):
    model = Info
    template_name = "index.html"
    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['query_results'] = self.get_queryset()
        return context

    def get_queryset(self):
        today = date.today()
        query_results = self.model.objects.filter(date__day = today.day).order_by('time')
        return query_results
