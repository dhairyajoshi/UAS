# Generated by Django 3.2.5 on 2021-12-25 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_alter_faculty_publications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='qualification',
            new_name='highest_qualification',
        ),
    ]
