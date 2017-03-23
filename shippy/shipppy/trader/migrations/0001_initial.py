# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trade_year',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('total_ton', models.IntegerField(blank=True, null=True)),
                ('total_value', models.IntegerField(blank=True, null=True)),
                ('usport', models.CharField(max_length=155)),
            ],
            options={
                'ordering': ['year'],
            },
        ),
    ]
