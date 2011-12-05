# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext
from django.template.loader import render_to_string

import simplejson as json

from emailkit.forms import ContactForm
from emailkit.utils import get_admin_email_addresses

def _send_email(form_data, template):
    # The form_data param should be an instance of form.cleaned_data
    message_body = render_to_string(template, form_data)

    try:
        send_mail(
            form_data['subject'],
            message_body,
            form_data['sender'],
            get_admin_email_addresses()
        )
    except Exception as e:
        print e

def contact_us(request):
    template = 'emailkit/{0}'
    if request.method == 'GET':
        return render(
            request,
            template.format('contact-us-form.html'),
                {'form': ContactForm()}
        )
    form = ContactForm(request.POST)
    if form.is_valid():
        _send_email(
            form.cleaned_data,
            template.format('email-contact-us.html')
        )
        html = render_to_string(
            template.format('thank-you-message.html'))
    else:
        html = render_to_string(
            template.format('contact-us-fields.html'),
                {'form': form},
            RequestContext(request)
        )
    json_dump = json.dumps({'html': html,
                            'is_valid': form.is_valid()}
    )
    return HttpResponse(
        json_dump,
        status=200,
        mimetype='application/json'
    )


