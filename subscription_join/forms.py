from crispy_forms.helper import FormHelper
from django import forms
from django.core.mail import send_mail
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field
import re
from crispy_forms.layout import Submit
from .models import NewsLetterUser, NewsLetter


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def send_mail(self):
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        # subject = 'From Prosnjit Localhost'
        # message = '%s %s' % (comment, name)
        emailFrom = self.cleaned_data['email']
        cc_myself = self.cleaned_data['cc_myself']
        emailTo = ['prosenjitearnkumar@gmail.com']
        send_mail(subject, message, emailFrom, emailTo, fail_silently=False,)


class CrispyContactAddressForm(ContactForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('subject', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('message', css_class='form-group col-md-6 mb-0'),
            ),
            'cc_myself',
            Submit('submit', 'Send')
        )


class NewsLetterUserSignUpForm(forms.Form):
    email = forms.EmailField()

    def clean_data(self):
        emailFrom = self.cleaned_data['email']
















