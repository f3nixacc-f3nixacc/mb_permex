import requests
from django.http import JsonResponse
from django.conf import settings

from permission_gateway.models import Platform, PlatformApplication, PlatformPermission


def receive_all_permissions(request):
	# if settings.SSO:
	#
	# response = requests.get(f"https://{settings.SSO['ROOT']}/api/permissions")
	#
	# 	return JsonResponse({"success": True, "res": response.json()})
	url = "http://localhost:8000/api/permissions"
	response = requests.get(f"{url}")

	if response.status_code != 200:
		return JsonResponse({"success": False, "res": response.json()})

	try:
		json_response = response.json()
		platform_name = list(json_response.keys())[0]

		if platform_name and platform_name in json_response:
			platform_data = format_data(json_response[platform_name])
			platform, created = Platform.objects.get_or_create(name=platform_name, url=url)
			for item in platform_data:
				platform_application, created = PlatformApplication.objects.get_or_create(platform=platform, name=item)
				for permission in platform_data[item]:
					PlatformPermission.objects.get_or_create(platform_application=platform_application, name=permission["name"], permission=permission["permission"])
	except Exception as e:
		return JsonResponse({"success": False, "res": str(e)})
	return JsonResponse({"success": True, "res": response.json()})

def format_data(data):
	platform_data = {}

	for item in data:
		formatted_name = format_name(item["content_type"]["app_label"])
		if formatted_name not in platform_data:
			platform_data[formatted_name] = []

		platform_data[formatted_name].append({
			"name": item["name"],
			"permission": item["codename"]
		})

	return platform_data

def format_name(name):
	formatted_name = name.split("_")
	formatted_name = " ".join(word.capitalize() for word in formatted_name)
	return formatted_name
