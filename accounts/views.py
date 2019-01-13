from django.shortcuts import render
from django.views.generic import FormView, TemplateView


class RegistrationView(TemplateView):
    template_name = 'accounts/registration.html'
