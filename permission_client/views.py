import json

from django.contrib.auth.models import Permission, Group, User
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@require_POST
@csrf_exempt
def get_user_groups(request):
	body = request.body.decode('utf-8')
	try:
		json_body = json.loads(body)
		user = User.objects.get(username=json_body["user"])
		user.groups.clear()
		for group in json_body["groups"]:
			group, created = Group.objects.get_or_create(name=group)
			user.groups.add(group)
		return JsonResponse("OK")
	except json.JSONDecodeError:
		return JsonResponse("Body is not valid JSON!")

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
def receive_permission_group(request):
	body = request.body.decode('utf-8')
	try:
		json_body = json.loads(body)
		Group.objects.get_or_create(name=json_body['permission_group_name'])
		return JsonResponse({"request.POST": json_body})
	except json.JSONDecodeError:
		return JsonResponse("Body is not valid JSON!")

@require_POST
@csrf_exempt
def receive_permission_groups(request):
	body = request.body.decode('utf-8')
	try:
		json_body = json.loads(body)
		for permission_group in json_body["permission_groups"]:
			if 'old' in permission_group and 'new' in permission_group:
				if 'action' in permission_group and permission_group['action'] == 'delete':
					Group.objects.filter(name=permission_group['new']).delete()
					continue

				if permission_group['old'] != permission_group['new']:
					Group.objects.filter(name=permission_group['old']).update(name=permission_group['new'])
				else:
					continue
				Group.objects.get_or_create(name=permission_group['new'])
			else:
				Group.objects.get_or_create(name=permission_group['new'])
		return JsonResponse({"request.POST": json_body})
	except json.JSONDecodeError:
		return JsonResponse("Body is not valid JSON!")

@require_POST
@csrf_exempt
def receive_permission_group_permissions(request):
	body = request.body.decode('utf-8')
	try:
		json_body = json.loads(body)
		for item in json_body:
			group, created = Group.objects.get_or_create(name=item)
			group.permissions.clear()
			for permission in json_body[item]:
				group.permissions.add(Permission.objects.get(codename=permission))
		return JsonResponse({"request.POST": json_body})
	except json.JSONDecodeError:
		return JsonResponse("Body is not valid JSON!")