# Generated by Django 3.1.2 on 2020-10-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sliderpost',
            options={'ordering': ['index', '-updated_on']},
        ),
        migrations.AddField(
            model_name='sliderpost',
            name='index',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]