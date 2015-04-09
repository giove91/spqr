# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_auto_20150330_1017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='keyword',
            options={'ordering': ('type', 'keyword')},
        ),
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ('russian', 'italian')},
        ),
        migrations.AddField(
            model_name='keyword',
            name='type',
            field=models.CharField(default=b'G', max_length=1, choices=[(b'G', b'Grammar'), (b'S', b'Subject')]),
            preserve_default=True,
        ),
    ]
