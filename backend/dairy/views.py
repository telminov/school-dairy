# coding=utf-8
from collections import OrderedDict
import rest_framework.viewsets
import rest_framework.mixins
from djutils.response import JSONResponse

from dairy import models
from dairy import serializers


class DayItemViewSet(rest_framework.mixins.ListModelMixin, rest_framework.viewsets.GenericViewSet):
    queryset = models.DayItem.objects.all()
    serializer_class = serializers.DayItem


def get_schedule(request):
    c = {
        'schedule': []
    }

    for i, day_name in models.ScheduleItem.DAY_OF_WEEK_CHOICES:
        day_data = {
            'name': day_name,
            'items': [],
        }

        for item in models.ScheduleItem.objects.filter(day_of_week=i):
            item_data = serializers.ScheduleItem(instance=item).data
            day_data['items'].append(item_data)

        c['schedule'].append(day_data)

    return JSONResponse(c)