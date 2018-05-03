# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]