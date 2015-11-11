# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('coopInfo', '0011_auto_20150304_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='picture',
            field=django_resized.forms.ResizedImageField(default=b'/media/persons/default.jpg', upload_to=b'persons'),
            preserve_default=True,
        ),
    ]
