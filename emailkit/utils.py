# -*- coding: utf-8 -*-
from django.conf import settings

def get_admin_email_addresses():
    """
    Generates a sequence consisting of admin e-mail addresses
    extracted from settings.ADMINS
    """
    return (admin[1] for admin in settings.ADMINS)
