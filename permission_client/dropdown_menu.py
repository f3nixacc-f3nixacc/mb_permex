import requests
from django.conf import settings
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _

API_URL = 'https://make-auth.com/api/v1/site_dropdown'
CACHE_TIMEOUT = 3600


def site_dropdown(request):
	if not request.user.is_authenticated:
		return []

	try:
		username = request.user.get_username()
		cache_key = f'site_dropdown:{username}'

		data = cache.get(cache_key)

		if data is None:
			response = requests.get(
				API_URL,
				params={'username': username},
				headers={'Authorization': f"Bearer {settings.SSO.get('TOKEN')}"},
				timeout=10,
			)
			response.raise_for_status()
			payload = response.json()

			data = [
				{
					'icon': item.get('icon', 'diamond'),
					'title': _(item['title']),
					'link': item['link'],
				}
				for item in payload
			]

			cache.set(cache_key, data, CACHE_TIMEOUT)

		return data
	except requests.exceptions.RequestException as ex:
		print(f'site_dropdown() API call failed: {ex}')
		return []
	except ValueError as ex:
		print(f'site_dropdown() JSON parsing error: {ex}')
		return []
	except Exception as ex:
		print(f'site_dropdown() error: {ex}')
		return []
