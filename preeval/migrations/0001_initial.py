# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('description', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('description', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('term', models.CharField(max_length=1, choices=[('1', '1er trimestre'), ('2', '2o trimestre'), ('3', '3er trimestre')])),
                ('study', models.CharField(max_length=1, choices=[('1', 'Malo'), ('2', 'Regular'), ('3', 'Malo')])),
                ('work', models.CharField(max_length=1, choices=[('1', 'Malo'), ('2', 'Regular'), ('3', 'Malo')])),
                ('attitude', models.CharField(max_length=1, choices=[('1', 'Malo'), ('2', 'Regular'), ('3', 'Malo')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Remarks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('term', models.CharField(max_length=1, choices=[('1', '1er trimestre'), ('2', '2o trimestre'), ('3', '3er trimestre')])),
                ('remarks', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=100)),
                ('group', models.ForeignKey(to='preeval.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('description', models.CharField(max_length=60)),
                ('group', models.ForeignKey(to='preeval.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(to='preeval.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='remarks',
            name='student',
            field=models.ForeignKey(to='preeval.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='remarks',
            name='subject',
            field=models.ForeignKey(to='preeval.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(to='preeval.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mark',
            name='subject',
            field=models.ForeignKey(to='preeval.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='level',
            field=models.ForeignKey(to='preeval.Level'),
            preserve_default=True,
        ),
    ]
