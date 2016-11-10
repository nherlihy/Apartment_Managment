from django.conf.urls import url
from app.views import public, dashboard, account

urlpatterns = [
	url(r'^$', public.home, name='home'),
	url(r'^dashboard.html/', dashboard.dashboard, name='dashboard'),
	url(r'^logout', account.log_out, name='logout'),
]