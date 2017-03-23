# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade_year',
            name='total_ton',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='trade_year',
            name='total_value',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
