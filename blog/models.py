from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.conf import settings
from django.dispatch import receiver

POST_STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


def compress(image):
    """
    Image compression method
    """
    image_name = image.name.split('/')[-1]
    im = Image.open(image)
    image_io = BytesIO()
    image_format = image.name.split('.')[-1]
    image_format = 'JPEG' if image_format.upper() == 'JPG' else image_format
    im.save(image_io, image_format, quality=60)
    new_image = File(image_io, name=image_name)
    return new_image


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.SET_NULL,
                               related_name='blog_posts', null=True)

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
    index = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['index', '-updated_on']

    def save(self, *args, **kwargs):
        self.image = compress(self.image)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.storage.delete(self.image.name)
        super().delete(*args, **kwargs)


@receiver(models.signals.pre_save, sender=SliderPost)
def delete_file_on_change_extension(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_image = SliderPost.objects.get(pk=instance.pk).image
        except SliderPost.DoesNotExist:
            return
        else:
            new_avatar = instance.image
            if old_image and old_image.url != new_avatar.url:
                old_image.delete(save=False)
