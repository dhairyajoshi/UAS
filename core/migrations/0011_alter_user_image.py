# Generated by Django 3.2.5 on 2021-12-31 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20211230_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='student_default.jpg', null=True, upload_to='StudentPics'),
        ),
    ]