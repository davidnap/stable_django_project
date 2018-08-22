from django.views.generic.base import TemplateView
from django.views.generic import FormView, ListView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django import forms
from results.models import Events
from django.utils import timezone

from django.views.generic.edit import CreateView
from results.models import Events
from django.views.generic.list import ListView

class Home(TemplateView):
    template_name = "index.html"

class EventCreate(CreateView):
    model = Events
    template_name = "index.html"
    success_url = "list"
    fields = ['title','message']

class Thanks(TemplateView):
    template_name = "thanks.html"

class ListItems(ListView):
    model = Events
    template_name = "index.html"
