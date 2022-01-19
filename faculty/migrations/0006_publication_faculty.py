# Generated by Django 3.2.5 on 2022-01-14 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0005_alter_faculty_teach_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faculty_publication', to='faculty.faculty'),
        ),
    ]