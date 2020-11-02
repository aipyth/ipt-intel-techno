from django.test import TestCase
from accounts.models import ScientificDirector, Section
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@email.com',
            password='foo12345678'
        )
        self.assertEqual(user.email, 'normal@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username shouldn't exist
            self.assertIsNone(user.username)
        except AttributeError:
            # is ok
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='foo12345678')

    def test_create_superuser(self):
        User = get_user_model()
        admin = User.objects.create_superuser('superuser@mail.com',
                                              'supersuper')
        self.assertEqual(admin.email, 'superuser@mail.com')
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
        try:
            # username shouldn't exist
            self.assertIsNone(admin.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='superuser@mail.com',
                password='supersuper',
                is_superuser=False
            )


class AccountsTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.sd = ScientificDirector.objects.create(name="Bill",
                                                    surname="Harrington")
        self.sec = Section.objects.create(name="Biology", short_name="BIO")
        self.sec.save()
        self.sd.save()

    def test_creation_director(self):
        self.assertEqual('Harrington Bill',
                         f"{self.sd.surname} {self.sd.name}")

    def test_creation_section(self):
        self.assertEqual('(BIO) Biology',
                         f"({self.sec.short_name}) {self.sec.name}")
