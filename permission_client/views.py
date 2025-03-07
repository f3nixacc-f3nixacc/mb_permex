from django.contrib.auth.models import Permission
from django.http import JsonResponse
from django.conf import settings


def get_all_permissions(request):
	if not hasattr(settings, 'SSO_APPLICATION_IDENTIFIER'):
		return JsonResponse({"success": False, "error": "SSO_APPLICATION_IDENTIFIER settings not set"})

	permissions = Permission.objects.all()

	permissions_data = [
		{
			"name": perm.name,
			"codename": perm.codename,
			"content_type": {
				"id": perm.content_type.id,
				"app_label": perm.content_type.app_label,
				"model": perm.content_type.model,
			},
		}
		for perm in permissions
	]
	permissions_data = {settings.SSO_APPLICATION_IDENTIFIER: permissions_data}
	return JsonResponse(permissions_data, safe=False)
