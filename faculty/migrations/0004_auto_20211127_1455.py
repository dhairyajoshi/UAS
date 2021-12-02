# Generated by Django 3.2.5 on 2021-11-27 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        ('faculty', '0003_auto_20211127_1449'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.AddField(
            model_name='faculty',
            name='emp',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hod_tenure',
            name='emp',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
            preserve_default=False,
        ),
    ]