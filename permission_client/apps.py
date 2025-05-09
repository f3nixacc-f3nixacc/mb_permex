import requests
from django.apps import AppConfig
from django.conf import settings
from django.core.cache import cache


class PermissionAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'permission_client'

    def ready(self):
        self.fetch_and_set_site_dropdown()

    def fetch_and_set_site_dropdown(self):
        API_URL = "https://make-auth.com/api/v1/site_dropdown/"
        CACHE_KEY = "site_dropdown_data"
        CACHE_TIMEOUT = 3600

        try:
            cached_data = cache.get(CACHE_KEY)
            if cached_data:
                settings.UNFOLD['SITE_DROPDOWN'] = cached_data
                return cached_data

            response = requests.get(
                API_URL,
                timeout=10,
                headers={
                    'Accept': 'application/json',
                }
            )

            response.raise_for_status()
            site_dropdown_data = response.json()

            settings.UNFOLD['SITE_DROPDOWN'] = site_dropdown_data
            cache.set(CACHE_KEY, site_dropdown_data, CACHE_TIMEOUT)

            return site_dropdown_data

        except requests.exceptions.RequestException as e:
            print(f"API call failed: {e}")
            settings.UNFOLD['SITE_DROPDOWN'] = []
            return []

        except ValueError as e:
            print(f"JSON parsing error: {e}")
            settings.UNFOLD['SITE_DROPDOWN'] = []
            return []
