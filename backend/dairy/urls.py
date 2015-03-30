# coding: utf-8
from django.conf.urls import url, patterns
from rest_framework import routers

from dairy import views

router = routers.DefaultRouter()
router.register('day_item', views.DayItemViewSet)

urlpatterns = router.urls

urlpatterns += patterns('dairy.views',
    url(r'^get_schedule/$', 'get_schedule'),
)