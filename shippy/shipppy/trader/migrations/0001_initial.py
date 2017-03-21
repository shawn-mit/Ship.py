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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('total_ton', models.IntegerField()),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'ordering': ['year'],
            },
        ),
        migrations.CreateModel(
            name='us_port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('year', models.ForeignKey(to='trader.trade_year')),
            ],
            options={
                'ordering': ['state'],
            },
        ),
    ]
