# Generated by Django 3.2.5 on 2021-11-23 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.branch'),
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
    ]
