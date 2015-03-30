# coding: utf-8

import rest_framework.serializers
from dairy import models

class DayItem(rest_framework.serializers.ModelSerializer):
    time_from = rest_framework.serializers.SerializerMethodField()
    time_to = rest_framework.serializers.SerializerMethodField()

    class Meta:
        model = models.DayItem

    def get_time_from(self, obj):
        return obj.time_from.strftime('%H:%M')

    def get_time_to(self, obj):
        return obj.time_to.strftime('%H:%M')

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