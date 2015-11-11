# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import coopInfo.models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('coopInfo', '0012_auto_20150304_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperative',
            name='mailAddress',
            field=models.CharField(max_length=80, verbose_name=b'mail address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='picture',
            field=django_resized.forms.ResizedImageField(default=b'/media/persons/default.jpg', upload_to=coopInfo.models.content_file_name),
            preserve_default=True,
        ),
    ]
