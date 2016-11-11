from django.conf.urls import url
from app.views import public, dashboard, account

urlpatterns = [
	url(r'^$', public.home, name='home'),
	url(r'^dashboard', dashboard.dashboard, name='dashboard'),
	url(r'^logout', account.log_out, name='logout'),
	url(r'^login', account.log_in, name='login'),
	url(r'^test', public.test, name='test'),
]