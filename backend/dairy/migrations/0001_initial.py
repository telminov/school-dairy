# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Классная работа',
            },
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Домашнее задание',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name_plural': 'Занятия',
                'verbose_name': 'Занятие',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Предметы',
                'verbose_name': 'Предмет',
            },
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('author', models.CharField(blank=True, max_length=255, verbose_name='Автор')),
                ('image', models.ImageField(blank=True, verbose_name='Обложка', upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Учебники',
                'verbose_name': 'Учебник',
            },
        ),
        migrations.AddField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(to='dairy.Subject'),
        ),
        migrations.AddField(
            model_name='homework',
            name='lesson',
            field=models.ForeignKey(to='dairy.Lesson'),
        ),
        migrations.AddField(
            model_name='homework',
            name='tutorial',
            field=models.ForeignKey(to='dairy.Tutorial'),
        ),
        migrations.AddField(
            model_name='classwork',
            name='lesson',
            field=models.ForeignKey(to='dairy.Lesson'),
        ),
        migrations.AddField(
            model_name='classwork',
            name='tutorial',
            field=models.ForeignKey(to='dairy.Tutorial'),
        ),
    ]
