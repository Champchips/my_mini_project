# Generated by Django 3.0.3 on 2020-03-11 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20200312_0322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll_vote',
            name='count',
        ),
        migrations.AlterField(
            model_name='poll',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 12, 3, 23, 14, 284284)),
        ),
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 12, 3, 23, 14, 284284)),
        ),
    ]
