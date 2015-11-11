# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coopInfo', '0014_auto_20150310_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='sex',
            field=models.CharField(default='M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=False,
        ),
    ]
