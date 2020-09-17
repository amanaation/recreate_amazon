from django.contrib import admin
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url(r'', views.render_page),
	url(r'^mydata$', views.google),
]

urlpatterns += staticfiles_urlpatterns()
