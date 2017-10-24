# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-24 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img', models.FileField(blank=True, null=True, upload_to='product_imgs')),
                ('fake_quality', models.IntegerField(default=0)),
                ('real_quality', models.IntegerField(default=0)),
                ('verified_quality', models.IntegerField(default=0)),
                ('percentage', models.FloatField(default=0.0)),
                ('coeff', models.FloatField(default=0.0)),
                ('price', models.FloatField(default=0.0)),
                ('amount', models.IntegerField(default=0)),
                ('experiment_num', models.IntegerField(default=0)),
            ],
        ),
    ]
