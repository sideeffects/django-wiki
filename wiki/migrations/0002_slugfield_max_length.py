# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlpath',
            name='slug',
            field=models.SlugField(max_length=100, null=True, verbose_name='slug', blank=True),
        ),
    ]
