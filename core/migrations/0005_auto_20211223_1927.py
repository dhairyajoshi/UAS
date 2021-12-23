# Generated by Django 3.2.5 on 2021-12-23 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_user_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='addresses',
            field=models.ManyToManyField(blank=True, related_name='user_addressdetails', to='core.AddressDetail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='education_details',
            field=models.ManyToManyField(blank=True, related_name='user_educationdetails', to='core.EducationDetail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.usergroup'),
        ),
    ]