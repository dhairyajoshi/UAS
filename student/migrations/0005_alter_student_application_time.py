# Generated by Django 3.2.5 on 2021-12-28 14:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20211228_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='application_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 28, 14, 52, 11, 396848, tzinfo=utc)),
            preserve_default=False,
        ),
    ]