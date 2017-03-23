# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0002_auto_20170322_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade_year',
            name='total_ton',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
        migrations.AlterField(
            model_name='trade_year',
            name='total_value',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]
