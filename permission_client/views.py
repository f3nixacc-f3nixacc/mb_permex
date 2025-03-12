from django.contrib.auth.models import Permission
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


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

@require_POST
@csrf_exempt
def receive_all_permissions(request):
	return JsonResponse({"test":"test"})


@require_POST
@csrf_exempt
def receive_all_teams(request):
	with open("test.txt", "a") as f:
		f.write(str(request.POST))
		f.write("\n")
		f.close()
	return JsonResponse({"request.POST":request.POST})