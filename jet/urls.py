import django
from django.conf.urls import url
from django.views.i18n import javascript_catalog

from jet.views import add_bookmark_view
from jet.views import edit_bookmark_view
from jet.views import remove_bookmark_view
from jet.views import toggle_application_pin_view
from jet.views import model_lookup_view

js_info_dict = {
    'packages': ('django.conf', 'django.contrib.admin', 'jet',),
}

urlpatterns = [
    url(
        r'^add_bookmark/$',
        add_bookmark_view,
        name='add_bookmark'
    ),
    url(
        r'^edit_bookmark/$',
        edit_bookmark_view,
        name='edit_bookmark'
    ),
    url(
        r'^remove_bookmark/$',
        remove_bookmark_view,
        name='remove_bookmark'
    ),
    url(
        r'^toggle_application_pin/$',
        toggle_application_pin_view,
        name='toggle_application_pin'
    ),
    url(
        r'^model_lookup/$',
        model_lookup_view,
        name='model_lookup'
    ),
    url(
        r'^jsi18n/$',
        javascript_catalog, js_info_dict,
        name='jsi18n'
    ),
]

if django.VERSION[:2] < (1, 8):
    from django.conf.urls import patterns
    urlpatterns = patterns('', *urlpatterns)
