from django.conf.urls import url
from app.views import public, account

urlpatterns = [
	url(r'^$', public.home, name='home'),
	url(r'^logout', account.log_out, name='logout'),
]