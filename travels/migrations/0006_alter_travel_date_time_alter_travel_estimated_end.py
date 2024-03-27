# Generated by Django 5.0.2 on 2024-03-24 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0005_alter_travel_date_time_alter_travel_estimated_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='travel',
            name='estimated_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
