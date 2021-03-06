"""we_are_social URL Configuration

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
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from hello import views
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from products import views as product_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.get_index),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),
    url(r'^products/$', product_views.all_products),
    # url(r'^blog/', include('reusable.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
       url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
