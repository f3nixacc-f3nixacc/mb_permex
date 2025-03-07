from django.contrib import admin
from unfold.admin import ModelAdmin
from permission_gateway.models import UserPlatformPermission


@admin.register(UserPlatformPermission)
class UserPlatformPermissionAdmin(ModelAdmin):
	pass