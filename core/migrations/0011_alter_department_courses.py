# Generated by Django 3.2.5 on 2021-12-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
        ('core', '0010_auto_20211222_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='courses',
            field=models.ManyToManyField(related_name='Dept_courses', to='academics.Course'),
        ),
    ]
