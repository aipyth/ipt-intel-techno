from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Section)
admin.site.register(models.ScientificDirector)
admin.site.register(models.Competitor)