from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Account


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username', 'first_name',
                    'last_name', 'is_admin',)
    list_filter = ('is_admin', 'email', 'first_name', 'last_name',)
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password')}),
        ('Personal info', {
            'fields': ('first_name', 'last_name')}),
        ('Permissions', {
            'fields': ('is_admin', 'is_staff', 'user_permissions')}),
        ('Groups', {'fields': ('groups',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'username', 'password1', 'password2',)}
         ),
        ('Permissions', {
            'fields': ('user_permissions',)}),
        ('Groups', {'fields': ('groups',)}),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Account, UserAdmin)


# Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)
