# Generated by Django 3.0.3 on 2020-03-10 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20200310_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 21, 52, 7, 740390)),
        ),
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 21, 52, 7, 740390)),
        ),
    ]
