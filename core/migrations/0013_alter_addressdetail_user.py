# Generated by Django 3.2.5 on 2022-01-01 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_addressdetail_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressdetail',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_details', to=settings.AUTH_USER_MODEL),
        ),
    ]
