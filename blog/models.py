from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.conf import settings

POST_STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

def compress(image):
    "Image compression method"
    im = Image.open(image)
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=60) 
    new_image = File(im_io, name=image.name)
    return new_image

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='blog_posts', null=True)
    
    title_image = models.ImageField(upload_to='title_images/%Y/%m/%d/')
    content = models.TextField()

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=POST_STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} ({self.created_on})"
    
    def save(self, *args, **kwargs):
        self.title_image = compress(self.title_image)
        super().save(*args, **kwargs)


class SliderPost(models.Model):
    title = models.CharField(max_length=80, blank=True)
    image = models.ImageField(upload_to='slider_images/%Y/%m/%d/')
    text = models.CharField(max_length=120, blank=True)
    active = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # new_image = compress(self.image)
        self.image = compress(self.image)
        super().save(*args, **kwargs)
