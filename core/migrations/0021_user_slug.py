# Generated by Django 3.2.5 on 2022-01-23 16:44

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_department_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='email', unique=True),
        ),
    ]
