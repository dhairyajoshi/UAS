# Generated by Django 3.2.5 on 2021-12-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_application',
            name='application_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='student_application',
            name='entrance_exam',
            field=models.CharField(choices=[('JEE-MAIN', 'JEE-MAIN'), ('OJEE', 'OJEE')], default='JEE-MAIN', max_length=50),
        ),
        migrations.AddField(
            model_name='student_application',
            name='is_Tfw',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=5),
        ),
        migrations.AddField(
            model_name='student_application',
            name='is_defence',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=5),
        ),
        migrations.AddField(
            model_name='student_application',
            name='is_green_card',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=5),
        ),
        migrations.AddField(
            model_name='student_application',
            name='is_pwd',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=5),
        ),
        migrations.AddField(
            model_name='student_application',
            name='mode',
            field=models.CharField(choices=[('REGULAR', 'REGULAR'), ('SELF-SUSTAINING', 'SELF-SUSTAINING')], default='REGULAR', max_length=50),
        ),
        migrations.AddField(
            model_name='student_application',
            name='parents_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='student_application',
            name='parents_mobile',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='student_application',
            name='status',
            field=models.CharField(choices=[('Accept', 'Accepted'), ('Reject', 'Not Accepted')], default='Reject', max_length=10),
        ),
    ]