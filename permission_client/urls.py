from django.urls import path

from permission_client.views import (
	get_all_permissions,
	receive_all_permissions,
	receive_team,
	receive_teams,
	receive_team_permissions
)

urlpatterns = [
	path('permissions/', get_all_permissions, name='get_all_permissions_from_child'),
	path('get_permissions/', receive_all_permissions, name='receive_permissions_from_host'),
	path('team/', receive_team, name='receive_single_team_from_host'),
	path('teams/', receive_teams, name='receive_all_teams_from_host'),
	path('team/permissions', receive_team_permissions, name='receive_team_permissions_from_host'),
]