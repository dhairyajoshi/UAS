# Generated by Django 3.2.5 on 2022-01-19 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20220119_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='application_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
