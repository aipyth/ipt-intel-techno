from django.db import models

POST_STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey('auth.User', on_delete= models.CASCADE,related_name='blog_posts')
    
    title_image = models.ImageField(upload_to='title_images/%Y/%m/%d/')
    content = models.TextField()

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=POST_STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} ({self.created_on})"


class SliderPost(models.Model):
    title = models.CharField(max_length=80, blank=True)
    image = models.ImageField(upload_to='slider_images/%Y/%m/%d/')
    text = models.CharField(max_length=120, blank=True)
    active = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
