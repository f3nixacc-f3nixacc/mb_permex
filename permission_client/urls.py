from django.urls import path

from permission_client.views import (
	get_all_permissions,
	receive_all_permissions,
	receive_permission_group,
	receive_permission_groups,
	receive_permission_group_permissions,
	get_user_groups
)

urlpatterns = [
	path('permissions/', get_all_permissions, name='get_all_permissions_from_child'),
	path('get_permissions/', receive_all_permissions, name='receive_permissions_from_host'),
	path('permission_group/', receive_permission_group, name='receive_single_permission_group_from_host'),
	path('permission_groups/', receive_permission_groups, name='receive_all_permission_groups_from_host'),
	path('permission_group/permissions/', receive_permission_group_permissions, name='receive_permission_group_permissions_from_host'),
	path('user_groups/', get_user_groups, name='get_user_groups'),
]
