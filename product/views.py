from django.shortcuts import render
from django.views.generic import TemplateView

from django.views import View

class InitialView(TemplateView):
    template_name = 'product/main.html'
