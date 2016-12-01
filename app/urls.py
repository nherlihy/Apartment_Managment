from django.conf.urls import url
from app.views import public, dashboard, account

app_name = 'app'
urlpatterns = [
	url(r'^$', public.home, name='home'),
	url(r'^logout', account.log_out, name='logout'),
	url(r'^login', account.log_in, name='login'),
	url(r'^register', account.register, name='register'),
	url(r'^create-group', account.create_group, name='create-group'),
	url(r'^add-group', account.add_to_group, name='add-group'),
	url(r'^ajax/add-expense', dashboard.ajax_add_expense, name='add-expense'),
	url(r'^profile', account.profile, name='profile'),
	url(r'^test', public.test, name='test'),
]