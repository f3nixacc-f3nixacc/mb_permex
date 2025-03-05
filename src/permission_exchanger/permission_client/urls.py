from django.urls import path

from src.permission_exchanger.permission_client.views import get_all_permissions

urlpatterns = [
	path('permissions/', get_all_permissions, name='get_all_permissions_from_child'),
]