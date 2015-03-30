# coding: utf-8

import rest_framework.serializers
from dairy import models

class DayItem(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = models.DayItem


class Subject(rest_framework.serializers.ModelSerializer):
    is_optional = rest_framework.serializers.SerializerMethodField()

    class Meta:
        model = models.Subject

    def get_is_optional(self, obj):
        return int(obj.is_optional)


class ScheduleItem(rest_framework.serializers.ModelSerializer):
    day_item = DayItem()
    subject = Subject()

    class Meta:
        model = models.ScheduleItem