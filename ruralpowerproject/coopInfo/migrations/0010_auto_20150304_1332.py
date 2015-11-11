# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coopInfo', '0009_auto_20150302_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='picture',
            field=models.ImageField(default=b'media/persons/default.jpg', upload_to=b'persons'),
            preserve_default=True,
        ),
    ]
