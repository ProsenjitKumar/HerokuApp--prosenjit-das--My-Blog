#from .mixins import AjaxFormMixin
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.shortcuts import render
from .models import NewsLetterUser, NewsLetter
from .forms import NewsLetterUserSignUpForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings


class ContactView(FormView):
    template_name = 'subscription_join/contact/contact.html'
    form_class = ContactForm
    success_url = '/success/'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        #context["testing_out"] = "this is a new context var"
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        #print "form is valid"

        form.send_mail()
        print("Form Is Valid")
        return super(ContactView, self).form_valid(form)


class Success(TemplateView):
    template_name = "subscription_join/contact/success.html"


class NewsLetterUserSignUpView(FormView):
    template_name = 'blog/base/base_blog.html'
    form_class = NewsLetterUserSignUpForm
    success_url = '/success/'

    def get_context_data(self, **kwargs):
        context = super(NewsLetterUserSignUpView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super(NewsLetterUserSignUpView, self).form_valid(form)

