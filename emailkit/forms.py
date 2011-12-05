# -*- coding: utf-8 -*-
from django import forms
from django.core.urlresolvers import reverse

from captcha.fields import CaptchaField
from uni_form.helper import FormHelper
from uni_form.layout import Layout, Div, Submit

class BaseEmailForm(forms.Form):
    sender = forms.EmailField(label=u'E-mail')
    sender_name = forms.CharField(max_length=100, label=u'Your Name')
    captcha = CaptchaField(label=u'Type the letters below')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        submit = Submit(u'submit',u'Submit')
        self.helper.add_input(submit)
        self.helper.form_method = u'POST'
        self.helper.form_class = u'uni_form'
        super(BaseEmailForm, self).__init__(*args, **kwargs)

class ContactForm(BaseEmailForm):

    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper.form_action = reverse(u'emailkit_contact_us')
        self.helper.form_id = u'contact-form'
        self.helper.add_layout(
            Div(
                Layout(
                    u'sender',
                    u'sender_name',
                    u'subject',
                    u'message',
                    u'captcha'
                ),
                css_id=u'form-fields'
            )
        )
