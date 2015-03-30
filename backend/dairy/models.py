# coding=utf-8
from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    is_optional = models.BooleanField(default=False, verbose_name='Внеурочная деятельность')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = 'is_optional', 'name',

    def __str__(self):
        label = self.name
        if self.is_optional:
            label += ' (внеурочка)'
        return label


class Tutorial(models.Model):
    subject = models.ForeignKey(Subject, verbose_name='Предмет')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    author = models.CharField(max_length=255, blank=True, verbose_name='Автор')
    image = models.ImageField(blank=True, verbose_name='Обложка')

    class Meta:
        verbose_name = 'Учебник'
        verbose_name_plural = 'Учебники'
        ordering = 'name',
        unique_together = 'name', 'author'

    def __str__(self):
        label = self.name
        if self.author:
            label += ' (%s)' % self.author
        return label


class Lesson(models.Model):
    subject = models.ForeignKey(Subject, verbose_name='Предмет')
    date = models.DateField(verbose_name='Дата')

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
        ordering = ('-date', 'subject__name')

    def __str__(self):
        return '%s %s' % (self.subject, self.date)


class Classwork(models.Model):
    lesson = models.ForeignKey(Lesson)
    tutorial = models.ForeignKey(Tutorial, verbose_name='Учебник', null=True, blank=True)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Классная работа'

    def __str__(self):
        return ', '.join(map(str, filter(bool, [self.lesson, self.tutorial])))


class Homework(models.Model):
    lesson = models.ForeignKey(Lesson)
    tutorial = models.ForeignKey(Tutorial, verbose_name='Учебник', null=True, blank=True)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Домашнее задание'

    def __str__(self):
        return ', '.join(map(str, filter(bool, [self.lesson, self.tutorial])))


class DayItem(models.Model):
    position = models.PositiveIntegerField(verbose_name='Порядковый номер', unique=True)
    time_from = models.TimeField(verbose_name='Время начала')
    time_to = models.TimeField(verbose_name='Время конца')

    class Meta:
        verbose_name = 'Элемент дня'
        verbose_name_plural = 'Элементы дня'
        ordering = 'position',

    def __str__(self):
        return '%s - %s' % (self.time_from.strftime('%H:%M'), self.time_to.strftime('%H:%M'))

class ScheduleItem(models.Model):
    DAY_OF_WEEK_CHOICES = (
        (1, 'Понедельник'),
        (2, 'Вторник'),
        (3, 'Среда'),
        (4, 'Четверг'),
        (5, 'Пятница'),
    )

    day_of_week = models.PositiveSmallIntegerField(choices=DAY_OF_WEEK_CHOICES, verbose_name='День недели')
    day_item = models.ForeignKey(DayItem, verbose_name='элемент дня')
    subject = models.ForeignKey(Subject, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Элемент расписание'
        verbose_name_plural = 'Расписание'
        ordering = 'day_of_week', 'day_item__position'

    def __str__(self):
        return '%s %s %s' % (self.get_day_of_week_display(), self.day_item.position, self.subject.name)
