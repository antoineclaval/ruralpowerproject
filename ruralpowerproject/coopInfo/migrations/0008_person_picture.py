# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coopInfo', '0007_auto_20150213_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='picture',
            field=models.ImageField(default=b'media/person/default.jpg', upload_to=b'person'),
            preserve_default=True,
        ),
    ]
