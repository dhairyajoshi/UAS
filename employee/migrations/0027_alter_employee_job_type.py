# Generated by Django 3.2.5 on 2022-01-20 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0026_alter_employee_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job_type',
            field=models.CharField(choices=[('Temporary', 'Temporary'), ('Permanent', 'Permanent')], max_length=50, null=True),
        ),
    ]
