# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='admin',
            field=models.ForeignKey(blank=True, to='api.Customer', related_name='shop'),
            preserve_default=True,
        ),
    ]
