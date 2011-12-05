from django.conf import settings
from django.http import QueryDict
from django.test import TestCase

from dingus import Dingus

from emailkit import views
from emailkit.utils import get_admin_email_addresses

META = {
    'CSRF_COOKIE_USED': False,
    'CSRF_COOKIE': None,
}

class ContactUsTest(TestCase):

    def test_required_fields(self):
        post_data = QueryDict(u'sender=&sender_name=&subject=&message=')
        response = views.contact_us(Dingus(META=META, METHOD='POST', POST=post_data))
        assert u'Please enter an e-mail address.' in response.content
        assert u'Please enter your name.' in response.content
        assert u'Please enter a subject.' in response.content
        assert u'Please enter a message below.' in response.content

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
