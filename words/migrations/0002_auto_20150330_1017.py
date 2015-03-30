# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='keyword',
            field=models.CharField(unique=True, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='word',
            name='keywords',
            field=models.ManyToManyField(to='words.Keyword', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='word',
            name='russian',
            field=models.CharField(unique=True, max_length=128),
            preserve_default=True,
        ),
    ]
