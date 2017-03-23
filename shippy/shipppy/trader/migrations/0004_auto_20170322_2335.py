# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0003_auto_20170322_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade_year',
            name='total_ton',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trade_year',
            name='total_value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
