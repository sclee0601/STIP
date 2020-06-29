"""VirginiaPolicyDatabaseProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from VirginiaPolicyDatabaseApp.ViewSets import BillViewSet, SessionViewSet

router = DefaultRouter()
router.register("listBills", BillViewSet)
router.register("listSessions", SessionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'listBills/(?P<year>\d+)', BillViewSet.as_view({'get': 'list', 'post': 'create'})),
    #url(r'listBills/(?P<year>\d+)/(?P<bill_number>\d+)$', BillViewSet.as_view({'get': 'list', 'post': 'create'})),
]

urlpatterns += router.urls
