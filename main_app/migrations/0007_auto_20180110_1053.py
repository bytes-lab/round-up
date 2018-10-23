# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-10 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20180109_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='marketing_email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='marketing_first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='marketing_last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='shop_customer_email',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='shop_owner_first_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='shop_owner_last_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
