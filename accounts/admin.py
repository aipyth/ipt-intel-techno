from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('firstname', 'lastname')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('firstname', 'lastname', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'groups', 'user_permissions')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')
        return ()
        #     return (
        #                 (None, {'fields': ('email', 'password')}),
        #                 ('Personal info', {'fields': ('firstname', 'lastname')}),
        #                 ('Permissions', {'fields': ('is_active', 'is_staff',    'is_superuser', 'groups', 'user_permissions')}),
        #             )
        # return self.fieldsets

# admin.site.register(models.Section)
# admin.site.register(models.ScientificDirector)
# admin.site.register(models.Competitor)