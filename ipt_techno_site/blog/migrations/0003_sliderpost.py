# Generated by Django 3.1.2 on 2020-10-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_title_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to='slider_images/%Y/%m/%d/')),
                ('text', models.CharField(max_length=280)),
                ('active', models.BooleanField(default=False)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]