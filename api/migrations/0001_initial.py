# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, related_name='customer', serialize=False)),
                ('address', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('message', models.TextField(blank=True)),
                ('photo', models.URLField(blank=True)),
                ('status', models.CharField(default='PE', choices=[('PE', 'Pending'), ('DE', 'Delivered'), ('PA', 'Paid')], max_length=2)),
                ('receiver', models.ForeignKey(to='api.Customer', related_name='received')),
                ('sender', models.ForeignKey(to='api.Customer', related_name='ordered')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.TextField()),
                ('identifier', models.CharField(unique=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(default='C', choices=[('O', 'Open'), ('C', 'Close'), ('T', 'Test')], max_length=1)),
                ('admin', models.ForeignKey(to='api.Customer', related_name='shop')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
