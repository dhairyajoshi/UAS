# Generated by Django 3.2.5 on 2021-12-22 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=50, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('credit', models.IntegerField()),
                ('contact_hours', models.IntegerField()),
                ('course_type', models.CharField(choices=[('THEORY', 'THEORY'), ('SESSIONAL', 'SESSIONAL')], max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='DailyClassReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_date', models.DateField(null=True)),
                ('class_time', models.TimeField(null=True)),
                ('topics_cover', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'DailyClassReports',
            },
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.IntegerField()),
                ('exam_type', models.CharField(choices=[('MIDSEM', 'MIDSEM'), ('ENDSEM', 'ENDSEM')], default='ENDSEM', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Examinations',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=10)),
                ('year_of_esht', models.CharField(max_length=4)),
                ('num_of_seats', models.IntegerField()),
                ('is_ugc_accre', models.BooleanField(default=False)),
                ('is_nb_accre', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Programs',
            },
        ),
        migrations.CreateModel(
            name='SemesterCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'SemesterCourses',
            },
        ),
        migrations.CreateModel(
            name='SemesterMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.IntegerField()),
                ('marks_obtained', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'SemesterMarks',
            },
        ),
        migrations.CreateModel(
            name='SemesterRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('sem_type', models.CharField(choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'SemesterRecords',
            },
        ),
    ]
