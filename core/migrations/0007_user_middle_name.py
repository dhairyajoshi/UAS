# Generated by Django 3.2.5 on 2021-12-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_user_user_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
