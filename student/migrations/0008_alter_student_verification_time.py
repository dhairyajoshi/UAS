# Generated by Django 3.2.5 on 2021-11-27 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20211127_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='verification_time',
            field=models.DateTimeField(default='0000-00-00 00:00'),
        ),
    ]
