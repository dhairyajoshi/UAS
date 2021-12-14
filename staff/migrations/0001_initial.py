# Generated by Django 3.2.5 on 2021-12-14 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0005_auto_20211214_1646'),
        ('core', '0004_auto_20211211_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_descr', models.CharField(max_length=100, null=True)),
                ('curr_posn', models.CharField(max_length=50, null=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.branch')),
                ('desg', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.designation')),
                ('emp', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'verbose_name_plural': 'Staffs',
            },
        ),
    ]
