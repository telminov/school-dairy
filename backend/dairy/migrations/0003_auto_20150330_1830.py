# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dairy', '0002_auto_20150325_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayItem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('position', models.PositiveIntegerField(verbose_name='Порядковый номер', unique=True)),
                ('time_from', models.TimeField(verbose_name='Время начала')),
                ('time_to', models.TimeField(verbose_name='Время конца')),
            ],
            options={
                'verbose_name_plural': 'Элементы дня',
                'verbose_name': 'Элемент дня',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='ScheduleItem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('day_of_week', models.PositiveSmallIntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница')], verbose_name='День недели')),
                ('day_item', models.ForeignKey(verbose_name='элемент дня', to='dairy.DayItem')),
            ],
            options={
                'verbose_name_plural': 'Расписание',
                'verbose_name': 'Элемент расписание',
                'ordering': ('day_of_week', 'day_item__position'),
            },
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name_plural': 'Занятия', 'verbose_name': 'Занятие', 'ordering': ('-date', 'subject__name')},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name_plural': 'Предметы', 'verbose_name': 'Предмет', 'ordering': ('is_optional', 'name')},
        ),
        migrations.AddField(
            model_name='subject',
            name='is_optional',
            field=models.BooleanField(default=False, verbose_name='Внеурочная деятельность'),
        ),
        migrations.AlterField(
            model_name='classwork',
            name='tutorial',
            field=models.ForeignKey(verbose_name='Учебник', to='dairy.Tutorial', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='tutorial',
            field=models.ForeignKey(verbose_name='Учебник', to='dairy.Tutorial', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(verbose_name='Предмет', to='dairy.Subject'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='name',
            field=models.CharField(verbose_name='Название', max_length=100),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='subject',
            field=models.ForeignKey(verbose_name='Предмет', to='dairy.Subject'),
        ),
        migrations.AlterUniqueTogether(
            name='tutorial',
            unique_together=set([('name', 'author')]),
        ),
        migrations.AddField(
            model_name='scheduleitem',
            name='subject',
            field=models.ForeignKey(verbose_name='Предмет', to='dairy.Subject'),
        ),
    ]
