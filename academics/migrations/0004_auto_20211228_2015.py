# Generated by Django 3.2.5 on 2021-12-28 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_auto_20211223_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyclassreport',
            name='student_present',
        ),
        migrations.RemoveField(
            model_name='semestermarks',
            name='student',
        ),
    ]
