# coding=utf-8
from django.contrib import admin
import dairy.models

admin.site.register(dairy.models.Subject)
admin.site.register(dairy.models.Tutorial)
admin.site.register(dairy.models.Lesson)
