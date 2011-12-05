from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse

from emailkit.utils import get_admin_email_addresses

from unittest2 import expectedFailure

class ContactUsTest(TestCase):

    def test_can_see_contact_us_page(self):
        response = self.client.get(reverse('emailkit_contact_us'))
        self.assertTemplateUsed(response, 'django_email_kit/contact-us-form.html')

    def test_email_required_error(self):
        response = self.client.post(reverse('main_view'))
        self.assertFormError(response, 'form', 'sender', 'This field is required.')

    def test_name_required_error(self):
        response = self.client.post(reverse('main_view'))
        self.assertFormError(response, 'form', 'sender_name', 'This field is required.')

    def test_subject_required_error(self):
        response = self.client.post(reverse('main_view'))
        self.assertFormError(response, 'form', 'subject', 'This field is required.')

    def test_message_required_error(self):
        response = self.client.post(reverse('main_view'))
        self.assertFormError(response, 'form', 'message', 'This field is required.')

    @expectedFailure
    def test_successful_send(self):
        raise

    @expectedFailure
    def test_sender_email_address_used_by_template(self):
        raise

    @expectedFailure
    def test_sender_name_used_by_template(self):
        raise

    @expectedFailure
    def test_message_used_by_template(self):
        raise

class UtilsTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.old_admins = settings.ADMINS
        settings.ADMINS = (
            ('Test Admin 1', 'test@example.com'),
            ('Test Admin 2', 'test2@example.com'),
        )

    @classmethod
    def tearDownClass(cls):
        settings.ADMINS = cls.old_admins
        self.assertEquals(2, len(settings.ADMINS))

    def test_get_admin_email_addresses_returns_correct_number_of_email_addresses(self):
        self.assertEquals(2, len(list(get_admin_email_addresses())))

    def test_get_admin_email_addresses_returns_email_addresses(self):
        emails = get_admin_email_addresses()
        self.assertIn('test@example.com', enumerate(emails).next())
        self.assertIn('test2@example.com', enumerate(emails).next())
