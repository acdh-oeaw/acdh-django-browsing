from django.apps import apps
from django.test import TestCase, Client
from django.contrib.auth.models import User

from archiv.models import Person


MODELS = list(apps.all_models["archiv"].values())
USER = {"username": "testuser", "password": "somepassword"}
client = Client()


class EntitiesTestCase(TestCase):
    fixtures = [
        "data.json",
    ]

    def setUp(self):
        User.objects.create_user(**USER)

    def test_001_smoke(self):
        self.assertTrue(1 + 1, 2)

    def test_002_smokey(self):
        self.assertTrue(Person.objects.all())

    def test_003_listviews(self):
        for x in MODELS:
            try:
                url = x.get_listview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_003_detailviews(self):
        for x in MODELS:
            item = x.objects.first()
            try:
                url = item.get_absolute_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {"pk": item.id})
                self.assertEqual(response.status_code, 200)
