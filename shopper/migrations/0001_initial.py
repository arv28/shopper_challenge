# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 20:50
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shopper',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+19999999999'. Should be 10 digit number.", regex='^\\+?1?\\d{10}$')])),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('application_date', models.DateField(db_index=True, default=django.utils.timezone.now)),
                ('workflow_state', models.CharField(default='applied', max_length=100)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
