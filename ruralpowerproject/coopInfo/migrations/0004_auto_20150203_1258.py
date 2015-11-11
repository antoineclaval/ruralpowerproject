# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coopInfo', '0003_auto_20150129_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooperative',
            name='is990present',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='streetAddress',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
    ]
