# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeaton', '0004_status_total_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=10)),
                ('member_1_name', models.CharField(max_length=30)),
                ('member_1_phone_no', models.IntegerField(max_length=10)),
                ('member_1_email', models.EmailField(max_length=30)),
                ('member_2_name', models.CharField(blank=True, max_length=30, null=True)),
                ('member_2_phone_no', models.IntegerField(blank=True, max_length=10, null=True)),
                ('member_2_email', models.EmailField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
