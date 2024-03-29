"""OnlineRetailer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

from .modules.products import views as product_views
from .modules.experiments import views as exp_views

urlpatterns = [
	# Admin site
	url(r'^admin/',
	    admin.site.urls),

	# Product list
	url(r'^$',
	    product_views.read_view, name='read'),
	url(r'^read1$',
	    product_views.read1_view, name='read1'),
	url(r'^read2$',
	    product_views.read2_view, name='read2'),
	url(r'^read3$',
	    product_views.read3_view, name='read3'),
	url(r'^read4$',
	    product_views.read4_view, name='read4'),
	url(r'^quiz/$',
	    product_views.quiz_view, name='quiz'),
	url(r'^list/$',
	    product_views.product_list_view, name='product_list'),
	url(r'^cart/$',
	    product_views.product_cart_view, name='cart'),
	url(r'^checkout/$',
	    product_views.product_confirmation_view, name='confirm'),
	url(r'^survey/$',
	    product_views.survey_view, name='survey'),
	url(r'^add/(?P<item_id>[0-9]+)/$',
	    product_views.add_to_cart, name='add_to_cart'),
	url(r'^remove/(?P<item_id>[0-9]+)/$',
	    product_views.remove_from_cart, name='remove_from_cart'),

	# Control room
	url(r'^control/$',
	    exp_views.exp_control_view, name='control'),
	url(r'^control/random/$',
	    exp_views.random, name='random'),
	url(r'^control/delete/$',
	    exp_views.delete, name='delete'),
	url(r'^control/clean/$',
	    exp_views.clean_session, name='clean'),
	url(r'^control/download_survey/$',
	    exp_views.download_survey, name='download_survey'),
	url(r'^control/download_data/$',
	    exp_views.download_data, name='download_data')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
