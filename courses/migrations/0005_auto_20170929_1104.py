# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20170928_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=140)),
            ],
        ),
        migrations.RenameModel(
            old_name='Tabla',
            new_name='City',
        ),
        migrations.DeleteModel(
            name='Tablita',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='ciudad',
            new_name='city',
        ),
        migrations.AddField(
            model_name='course',
            name='city',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.City'),
        ),
        migrations.AddField(
            model_name='course',
            name='country',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Country'),
        ),
    ]
