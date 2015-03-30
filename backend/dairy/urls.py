# coding: utf-8
from django.conf.urls import url, include
from rest_framework import routers

from dairy import views

router = routers.DefaultRouter()
router.register('day_item', views.DayItemViewSet)

urlpatterns = router.urls