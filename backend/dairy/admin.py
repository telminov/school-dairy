# coding=utf-8
from django.contrib import admin
import dairy.models

admin.site.register(dairy.models.Subject)
admin.site.register(dairy.models.Tutorial)
admin.site.register(dairy.models.DayItem)
admin.site.register(dairy.models.ScheduleItem)


class ClassworkInline(admin.TabularInline):
    model = dairy.models.Classwork
    extra = 1

class HomeworkInline(admin.TabularInline):
    model = dairy.models.Homework
    extra = 1

class Lesson(admin.ModelAdmin):
    list_display = ('subject', 'date')
    inlines = (ClassworkInline, HomeworkInline)

admin.site.register(dairy.models.Lesson, Lesson)
