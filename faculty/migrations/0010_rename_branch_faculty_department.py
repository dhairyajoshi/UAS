# Generated by Django 3.2.5 on 2022-01-19 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0009_alter_publication_faculty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='branch',
            new_name='department',
        ),
    ]
