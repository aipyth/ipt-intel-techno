from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Document, DocPage


class DocPageAdmin(SummernoteModelAdmin):
    list_display = ('name', )
    list_per_page = 10
    search_fields = ['name', 'text']
    summernote_fields = ['text']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(DocPage, DocPageAdmin)
admin.site.register(Document)