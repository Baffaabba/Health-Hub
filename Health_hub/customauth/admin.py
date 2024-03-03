from django.contrib import admin
from .models import CustomUser, UserDetails

# class UserDetailsInline(admin.StackedInline):
#     model = UserDetails

# class UserCarInline(admin.StackedInline):
#     model = Car

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm

#     model = CustomUser

#     list_display = ('email', 'is_active',
#                     'is_staff', 'is_superuser', 'last_login',)
#     list_filter = ('is_active', 'is_staff', 'is_superuser')
#     fieldsets = (
#         (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
#         ('Permissions', {'fields': ('is_driver', 'is_staff', 'is_active',
#          'is_superuser', 'groups', 'user_permissions')}),
#         ('Dates', {'fields': ('last_login',)}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
#          ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     inlines = [
#         UserDetailsInline,
#         UserCarInline,
#     ]

admin.site.register(CustomUser)
admin.site.register(UserDetails)