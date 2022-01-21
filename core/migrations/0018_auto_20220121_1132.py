# Generated by Django 3.2.5 on 2022-01-21 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0005_auto_20220119_2322'),
        ('core', '0017_department_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, related_name='Dept_courses', to='academics.Course'),
        ),
        migrations.AlterField(
            model_name='department',
            name='programme',
            field=models.ManyToManyField(blank=True, null=True, related_name='branch_programme', to='academics.Program'),
        ),
    ]
