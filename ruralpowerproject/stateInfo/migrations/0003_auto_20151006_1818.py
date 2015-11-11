# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stateInfo', '0002_auto_20151006_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='population',
        ),
        migrations.AddField(
            model_name='county',
            name='state',
            field=models.ForeignKey(default=1, to='stateInfo.State'),
            preserve_default=False,
        ),
    ]
