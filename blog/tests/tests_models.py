from django.test import TestCase
from blog.models import Post, SliderPost
from django.contrib.auth import get_user_model


class BlogTestClass(TestCase):
    @classmethod
    def setUpTestData(self):
        user = get_user_model()
        with open('logo.png', 'rb') as testimage:
            admin = user.objects.create_superuser(
                'superuser@mail.com', 'supersuper')
            self.testpost = Post.objects.create(
                title='info', slug='info', author=admin,
                content='244466666', status=0, title_image=testimage)
            self.testpost.save()
            self.testslider = SliderPost.objects.create(
                title='title', text='sometext', image=testimage)
            self.testslider.save()

    def test_created_properly(self):
        self.assertTrue(isinstance(self.testpost, Post))
        self.assertEqual(self.testpost.__str__(),
                         f"{self.testpost.title} ({self.testpost.created_on})")

    def test_slider_creation(self):
        self.assertTrue(isinstance(self.testslider, SliderPost))
        self.assertEqual(self.testslider.active, False)
