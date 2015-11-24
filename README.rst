=======================
Django Views ACL plugin
=======================

Views ACL plugin is a Django app to provide method for automatic permissions
generation based on urlpatterns in urls.py

Quick start
-----------

1. Add "view_acl" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'view_acl',
    )

2. Provide method for automatic permissions generation based on urlpatterns in urls.py.

   `view_acl.autodiscovery()`.

3. Provision additional auth backend for blocking all views by default.
   Exclusion list is also provided for such views like login, logout, admin,
   etc + other customizable by user.

4. Name of permission is taken from `name=` parameter in `urlpatterns` record
   for each active view.
