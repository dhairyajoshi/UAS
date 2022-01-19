# Generated by Django 3.2.5 on 2022-01-14 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0020_alter_employee_job_type'),
        ('faculty', '0005_alter_faculty_teach_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
    ]