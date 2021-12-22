# Generated by Django 3.2.5 on 2021-12-22 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
        ('student', '0008_merge_20211220_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.course'),
        ),
        migrations.AlterField(
            model_name='student_application',
            name='course',
            field=models.ManyToManyField(related_name='student_applicant_courses', to='academics.Program'),
        ),
    ]
