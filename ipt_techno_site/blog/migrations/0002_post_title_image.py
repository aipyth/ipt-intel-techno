# Generated by Django 3.1.1 on 2020-09-30 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_image',
            field=models.ImageField(default=None, upload_to='title_images/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
