"""tap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from app_mgr import views

urlpatterns = [
    # USER AUTHENTICATION
    url(r'^register/', views.register, name='register'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^user_profile$', views.view_profile, name='view_profile'),
    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.reset_confirm, name='reset_confirm'),
    url(r'^reset/$', views.reset, name='reset'),
    url(r'^reset/sent/$', views.reset_sent, name='reset_sent'),

    #RESTFUL API
    url(r'^users/$', views.UserProfileListView.as_view(), name='user-list'),
    url(r'^orgs/$', views.OrganizationListView.as_view(), name='org-list'),
    url(r'^apps/$', views.ApplicationListView.as_view(), name='app-list'),

    url(r'^user/(?P<pk>[\d]+)/$', views.UserProfileInstanceView.as_view(), name='user-instance'),
    url(r'^user/(?P<pk>current)/$', views.UserProfileInstanceView.as_view(), name='user-current'),
    url(r'^org/(?P<pk>[\d]+)/$', views.OrganizationInstanceView.as_view(), name='org-instance'),
    url(r'^app/(?P<pk>[\d]+)/$', views.ApplicationInstanceView.as_view(), name='app-instance'),
]
