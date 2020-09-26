from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_per_page = 10
    list_filter = ("status",)
    search_fields = ['title', 'content']
    summernote_fields = ['content']
    readonly_fields = ['author']
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
