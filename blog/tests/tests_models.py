from django.test import TestCase
from blog.models import Post
from django.contrib.auth import get_user_model

class BlogTestClass(TestCase):
    @classmethod
    def setUpTestData(self):
        user = get_user_model()
        author_user = user.objects.create_user(first_name = 'author',username = 'authoruser',password = '123')
        self.testpost = Post.objects.create(
            title = 'Post 1', author = author_user,content = '244466666', 
            status = 0)
        self.testpost.save()
    
    def test_created_properly(self):
        self.assertTrue(isinstance(self.testpost, Post))
        self.assertEqual(self.testpost.__str__(), f"{self.testpost.title} ({self.testpost.created_on})")
