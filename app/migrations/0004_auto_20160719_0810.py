# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_statecapital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='capital',
        ),
        migrations.RemoveField(
            model_name='state',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='state',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='state',
            name='population',
        ),
        migrations.AddField(
            model_name='statecapital',
            name='state',
            field=models.OneToOneField(null=True, to='app.State'),
        ),
    ]
