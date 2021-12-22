# Generated by Django 3.2.5 on 2021-12-22 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0009_alter_department_options'),
        ('student', '0008_merge_20211220_2236'),
        ('faculty', '0010_alter_faculty_user'),
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
                ('dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_department', to='core.department')),
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
                ('fclt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clsrpt_fcltydetails', to='faculty.faculty')),
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
                ('dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Exam_deptdetail', to='core.department')),
            ],
            options={
                'verbose_name_plural': 'Examinations',
            },
        ),
        migrations.CreateModel(
            name='SemesterCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sem_coursedetails', to='academics.course')),
                ('daily_class_report', models.ManyToManyField(related_name='sem_course_daily_class_report', to='academics.DailyClassReport')),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semcourse_fcltydetails', to='faculty.faculty')),
            ],
            options={
                'verbose_name_plural': 'SemesterCourses',
            },
        ),
        migrations.CreateModel(
            name='SemesterRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('sem_type', models.CharField(choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], max_length=10, null=True)),
                ('dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.department')),
                ('sem_course', models.ManyToManyField(related_name='sem_rec_sem_coursedetail', to='academics.SemesterCourse')),
                ('student', models.ManyToManyField(related_name='sem_rec_studentdetail', to='student.Student')),
            ],
            options={
                'verbose_name_plural': 'SemesterRecords',
            },
        ),
        migrations.CreateModel(
            name='SemesterMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.IntegerField()),
                ('marks_obtained', models.IntegerField()),
                ('dept', models.ManyToManyField(related_name='semmarks_deptdetails', to='core.Department')),
                ('exam', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.examination')),
                ('fclt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semmarks_fcltydetails', to='faculty.faculty')),
                ('sem_course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semmark_coursedetails', to='academics.semestercourse')),
                ('student', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.student')),
            ],
            options={
                'verbose_name_plural': 'SemesterMarks',
            },
        ),
        migrations.AddField(
            model_name='semestercourse',
            name='sem_record',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.semesterrecord'),
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
                ('departments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_department', to='core.department')),
            ],
            options={
                'verbose_name_plural': 'Programs',
            },
        ),
        migrations.AddField(
            model_name='examination',
            name='sem_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_semcoursedetails', to='academics.semestercourse'),
        ),
        migrations.AddField(
            model_name='examination',
            name='sem_rec',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_semrecdeetails', to='academics.semesterrecord'),
        ),
        migrations.AddField(
            model_name='dailyclassreport',
            name='sem_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clsrpt_semcoursedetails', to='academics.semestercourse'),
        ),
        migrations.AddField(
            model_name='dailyclassreport',
            name='student_prsnt',
            field=models.ManyToManyField(related_name='clsrpt_Studentdetail', to='student.Student'),
        ),
    ]
