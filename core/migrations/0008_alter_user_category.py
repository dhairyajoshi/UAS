# Generated by Django 3.2.5 on 2021-12-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_user_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='category',
            field=models.CharField(choices=[('General', 'General'), ('SC', 'SC'), ('ST', 'ST'), ('OBC', 'OBC'), ('SEBC', 'SEBC')], max_length=50, null=True),
        ),
    ]