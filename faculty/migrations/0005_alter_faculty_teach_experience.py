# Generated by Django 3.2.5 on 2021-12-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_rename_qualification_faculty_highest_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='teach_experience',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
