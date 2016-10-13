from django.conf.urls import url
from app.views import public

urlpatterns = [
	url(r'^$', public.home, name='home'),
]