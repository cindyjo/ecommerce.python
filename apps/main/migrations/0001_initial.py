# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.TextField(max_length=45)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
