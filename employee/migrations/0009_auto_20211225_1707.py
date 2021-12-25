# Generated by Django 3.2.5 on 2021-12-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_alter_employee_job_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='post',
        ),
        migrations.AlterField(
            model_name='employee',
            name='job_type',
            field=models.CharField(choices=[('Temporary', 'Temporary'), ('Permanent', 'Permanent')], max_length=50, null=True),
        ),
    ]
