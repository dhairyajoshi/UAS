# Generated by Django 3.2.5 on 2021-12-20 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_role'),
        ('faculty', '0008_auto_20211217_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
    ]