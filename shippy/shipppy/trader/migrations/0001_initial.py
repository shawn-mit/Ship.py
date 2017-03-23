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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('total_ton', models.IntegerField()),
                ('total_value', models.IntegerField()),
                ('usport', models.CharField(max_length=155)),
            ],
            options={
                'ordering': ['year'],
            },
        ),
    ]
