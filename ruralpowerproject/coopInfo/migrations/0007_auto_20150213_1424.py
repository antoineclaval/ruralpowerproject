# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coopInfo', '0006_auto_20150213_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperative',
            name='consumers',
            field=models.IntegerField(default=0, null=True, verbose_name=b'number of consumers', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='milesOfLines',
            field=models.IntegerField(default=0, null=True, verbose_name=b'miles of electric lines', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='numberOfEmployees',
            field=models.IntegerField(default=0, null=True, verbose_name=b'number of employees', blank=True),
            preserve_default=True,
        ),
    ]
