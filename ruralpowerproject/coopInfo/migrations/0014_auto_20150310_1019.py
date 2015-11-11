# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coopInfo', '0013_auto_20150309_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperative',
            name='email',
            field=models.CharField(max_length=60, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='nextElectionTerms',
            field=models.CharField(max_length=60, verbose_name=b'next election', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='phone',
            field=models.CharField(max_length=70, blank=True),
            preserve_default=True,
        ),
    ]
