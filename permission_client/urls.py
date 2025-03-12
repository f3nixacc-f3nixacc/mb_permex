from django.urls import path

from permission_client.views import get_all_permissions, receive_all_permissions, receive_team

urlpatterns = [
	path('permissions/', get_all_permissions, name='get_all_permissions_from_child'),
	path('get_permissions/', receive_all_permissions, name='receive_permissions_from_host'),
	path('team/', receive_team, name='receive_single_team_from_host'),
]