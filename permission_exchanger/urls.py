from django.urls import path

from permission_exchanger.views import get_all_permissions, receive_all_permissions

urlpatterns = [
	path('permissions/', get_all_permissions, name='get_all_permissions_from_child'),
	path('adopt_permissions/', receive_all_permissions, name='receive_all_permissions_from_child'),
]