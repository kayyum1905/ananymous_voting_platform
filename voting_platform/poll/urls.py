from django.conf.urls import url

from . import views


urlpatterns = [
    url('^$', views.submit_form, name='submit'),
]