=====
Permission exchanger
=====

The app that will give your django application ability to exchange permissions between Django platforms

Quick start
-----------

1. Add "XXX" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'XXX',
    ]

2. Include the polls URLconf in your project urls.py like this::

    urlpatterns += [path('api/', include('permission_client.urls'))] # FOR CLIENT

