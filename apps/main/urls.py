from django.conf.urls import patterns, url
from apps.main import views
urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^cart/$', views.cart, name='cart'),
	url(r'^process/$', views.process_form, name='process'),
	url(r'^orders/(?P<order_id>\d+)/$', views.destroy, name="destroy"),
)