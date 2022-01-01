# Generated by Django 3.2.5 on 2022-01-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_addressdetail_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressdetail',
            name='address_type',
            field=models.CharField(blank=True, choices=[('PRESENT', 'PRESENT'), ('PERMANENT', 'PERMANENT')], max_length=100, null=True),
        ),
    ]
