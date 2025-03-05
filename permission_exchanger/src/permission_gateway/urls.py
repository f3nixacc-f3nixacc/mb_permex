from django.urls import path

from permission_exchanger.src.permission_gateway.views import receive_all_permissions

urlpatterns = [
	path('adopt_permissions/', receive_all_permissions, name='receive_all_permissions_from_child'),
]