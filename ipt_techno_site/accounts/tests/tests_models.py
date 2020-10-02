from django.test import TestCase
from accounts.models import ScientificDirector, Section

class AccountsTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.sd =ScientificDirector.objects.create(name = "Bill", surname = "Harrington")
        self.sd.save()
        self.sec = Section.objects.create(name = "Biology", short_name="BIO")
        self.sec.save()
    def test_creation_director(self):
        self.assertEqual('Harrington Bill',f"{self.sd.surname} {self.sd.name}")
    def test_creation_section(self):
        self.assertEqual('(BIO) Biology', f"({self.sec.short_name}) {self.sec.name}")