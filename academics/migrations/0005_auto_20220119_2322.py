# Generated by Django 3.2.5 on 2022-01-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0004_auto_20211228_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='contact_hours',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='credit',
            field=models.IntegerField(null=True),
        ),
    ]