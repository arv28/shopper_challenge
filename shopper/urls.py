from django.conf.urls import url

from . import views

app_name = 'shopper'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^confirmation/$', views.confirmation, name='confirmation'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login/$', views.login, name='login'),
    #url(r'^edit/$', views.edit, name='edit'),
]
