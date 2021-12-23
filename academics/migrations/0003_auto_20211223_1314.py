# Generated by Django 3.2.5 on 2021-12-23 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_auto_20211223_1314'),
        ('core', '0001_initial'),
        ('student', '0002_auto_20211223_1314'),
        ('academics', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examination',
            old_name='dept',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='examination',
            old_name='sem_rec',
            new_name='sem_record',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='is_nb_accre',
            new_name='is_nb_accredeted',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='is_ugc_accre',
            new_name='is_ugc_accredeted',
        ),
        migrations.RenameField(
            model_name='semesterrecord',
            old_name='dept',
            new_name='department',
        ),
        migrations.RemoveField(
            model_name='dailyclassreport',
            name='student_prsnt',
        ),
        migrations.AddField(
            model_name='dailyclassreport',
            name='student_present',
            field=models.ManyToManyField(related_name='classreport_Studentdetail', to='student.Student'),
        ),
        migrations.AlterField(
            model_name='dailyclassreport',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classreport_facultydetails', to='faculty.faculty'),
        ),
        migrations.AlterField(
            model_name='dailyclassreport',
            name='sem_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classreport_semcoursedetails', to='academics.semestercourse'),
        ),
        migrations.AlterField(
            model_name='semestercourse',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semcourse_facultydetails', to='faculty.faculty'),
        ),
        migrations.AlterField(
            model_name='semestermarks',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semmarks_departmentdetails', to='core.department'),
        ),
        migrations.AlterField(
            model_name='semestermarks',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semmarks_facultydetails', to='faculty.faculty'),
        ),
        migrations.AlterField(
            model_name='semesterrecord',
            name='sem_course',
            field=models.ManyToManyField(related_name='sem_record_sem_coursedetail', to='academics.SemesterCourse'),
        ),
        migrations.AlterField(
            model_name='semesterrecord',
            name='student',
            field=models.ManyToManyField(related_name='sem_record_studentdetail', to='student.Student'),
        ),
    ]
