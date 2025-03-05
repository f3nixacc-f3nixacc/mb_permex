import requests
from django.http import JsonResponse
from django.conf import settings


def receive_all_permissions(request):
	if settings.SSO:
		response = requests.get(f"https://{settings.SSO['ROOT']}/api/permissions")

		return JsonResponse({"success": True, "res": response.json()})

	return JsonResponse({"success": False})
