# Generated by Django 3.2.5 on 2021-12-14 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_auto_20211212_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='quaification',
            new_name='qualification',
        ),
    ]