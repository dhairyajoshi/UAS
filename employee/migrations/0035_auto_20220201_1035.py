# Generated by Django 3.2.5 on 2022-02-01 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0034_alter_employee_job_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leavetype',
            name='leave',
        ),
        migrations.AddField(
            model_name='leave',
            name='leave_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emp_leave_type', to='employee.leavetype'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job_type',
            field=models.CharField(choices=[('Temporary', 'Temporary'), ('Permanent', 'Permanent')], max_length=50, null=True),
        ),
    ]
