# coding: utf-8

import rest_framework.serializers
from dairy import models

class DayItem(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = models.DayItem