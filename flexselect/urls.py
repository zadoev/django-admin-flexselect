from django.conf.urls import url
from flexselect.views import field_changed


urlpatterns = [
    url(r'field_changed', field_changed, name='flexselect_field_changed'),
]
