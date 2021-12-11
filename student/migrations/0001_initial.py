# Generated by Django 3.2.5 on 2021-12-11 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jee_roll', models.CharField(max_length=100, null=True)),
                ('jee_rank', models.CharField(max_length=100, null=True)),
                ('programme', models.CharField(choices=[('B.Tech.', 'B.Tech.')], max_length=50, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.branch')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification_time', models.DateTimeField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('verified_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
