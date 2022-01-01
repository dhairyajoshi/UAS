# Generated by Django 3.2.5 on 2022-01-01 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0017_alter_employee_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job_type',
            field=models.CharField(choices=[('Permanent', 'Permanent'), ('Temporary', 'Temporary')], max_length=50, null=True),
        ),
    ]
