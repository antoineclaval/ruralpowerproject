# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coopInfo', '0002_auto_20150128_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperative',
            name='consumers',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='milesOfLines',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='numberOfEmployees',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
    ]
