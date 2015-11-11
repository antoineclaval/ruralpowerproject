# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stateInfo', '0003_auto_20151006_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='state',
            field=models.ForeignKey(default=1, to='stateInfo.State'),
            preserve_default=True,
        ),
    ]
