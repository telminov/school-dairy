# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dairy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Предмет', 'ordering': ('name',), 'verbose_name_plural': 'Предметы'},
        ),
        migrations.AlterModelOptions(
            name='tutorial',
            options={'verbose_name': 'Учебник', 'ordering': ('name',), 'verbose_name_plural': 'Учебники'},
        ),
        migrations.AddField(
            model_name='tutorial',
            name='subject',
            field=models.ForeignKey(to='dairy.Subject', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='description',
            field=models.TextField(verbose_name='Описание', blank=True),
        ),
    ]
