=====
Permission exchanger
=====

The app that will give your django application ability to exchange permissions between Django platforms

Quick start
-----------

1. Add `"XXX"` to your `INSTALLED_APPS` settings like this::

       INSTALLED_APPS = [
           ...
           "XXX",
       ]

2. Add `"SITE_DROPDOWN"` to your `UNFOLD` settings like this::

       UNFOLD = {
           ...
           "SITE_DROPDOWN": "permission_client.dropdown_menu.site_dropdown",
       }

3. Make sure you have SSO settings with key `"TOKEN"` like this::

       SSO = {
           ...
           "TOKEN": ...
       }

4. Include the polls URLconf in your project `urls.py` like this::

       urlpatterns += [path('api/', include('permission_client.urls'))]  # FOR CLIENT

