from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^signin$', views.signin),
    # url(r'^dashboard$', views.dashboard),

    # url(r'^logoff$', views.logout),
    # url(r'register/create$', views.create_user),
    # url(r'^register/create$', views.create_user),
    # url(r'^users/new/add$', views.admin_create_user),
    # url(r'^users/edit/(?P<user_id>\d+)/update_user$', views.update_user),
    # url(r'^users/edit/(?P<user_id>\d+)/update_password$', views.update_password),

]