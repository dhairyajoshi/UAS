# Generated by Django 3.2.5 on 2021-12-25 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_employee_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='pan_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='work_email_id',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='work_phone_number',
            field=models.CharField(max_length=14, null=True),
        ),
    ]
