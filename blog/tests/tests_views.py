from django.test import TestCase
from blog.models import Post
from django.contrib.auth import get_user_model

class BlogPageTest(TestCase):
    # @classmethod
    # def setUpTestData(self):
    
    #     user = get_user_model()
    #     admin = user.objects.create_superuser('superuser@mail.com', 'supersuper')
    #     self.testpost = Post.objects.create(
    #             title = 'info',slug = 'info', author = admin,content='244466666', 
    #             status = 0)
    #     self.testpost.save()
  
    def test_home_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
              
    def test_posts_page_exist(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
    
    #def test_exact_post_exist(self):
     #TODO   response = self.client.get('info')
     #  self.assertEqual(responce.status_code, 200)

    def test_home_templates(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/index.html')
    
    def test_posts_templates(self):
        responce = self.client.get('/posts/')
        self.assertTemplateUsed(responce, 'blog/post_list.html')
    