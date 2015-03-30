# coding=utf-8
from django.shortcuts import render
import rest_framework.viewsets
import rest_framework.mixins

from dairy import models
from dairy import serializers

class DayItemViewSet(rest_framework.mixins.ListModelMixin, rest_framework.viewsets.GenericViewSet):
    queryset = models.DayItem.objects.all()
    serializer_class = serializers.DayItem