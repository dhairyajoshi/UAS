# Generated by Django 3.2.5 on 2022-01-01 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_addressdetail_address_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressdetail',
            name='address_type',
            field=models.CharField(blank=True, choices=[('Present', 'Present'), ('Permanent', 'Permanent')], max_length=100, null=True),
        ),
    ]