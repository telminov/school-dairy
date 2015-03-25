# coding=utf-8
from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = 'name',

    def __str__(self):
        return self.name


class Tutorial(models.Model):
    subject = models.ForeignKey(Subject, verbose_name='Предмет')
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    author = models.CharField(max_length=255, blank=True, verbose_name='Автор')
    image = models.ImageField(blank=True, verbose_name='Обложка')

    class Meta:
        verbose_name = 'Учебник'
        verbose_name_plural = 'Учебники'
        ordering = 'name',

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
    tutorial = models.ForeignKey(Tutorial)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Классная работа'

    def __str__(self):
        return '%s %s' % (self.lesson, self.tutorial)


class Homework(models.Model):
    lesson = models.ForeignKey(Lesson)
    tutorial = models.ForeignKey(Tutorial)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Домашнее задание'

    def __str__(self):
        return '%s %s' % (self.lesson, self.tutorial)