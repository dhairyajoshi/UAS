from django.db import models
from django.db.models.base import Model
from django.db.models.fields import related
from django.utils import tree
from core import models as core_models
from faculty import models as faculty_models
from student import models as student_models
# Create your models here.

COURSE_TYPE_CHOICES=(
    ('THEORY','THEORY'),
    ('SESSIONAL','SESSIONAL')
)

SEMESTER_CHOICES=(
    ('ODD','ODD'),
    ('EVEN','EVEN')
)

EXAMINATION_CHOICES=(
    ('MIDSEM','MIDSEM'),
    ('ENDSEM','ENDSEM')
)

class Program(models.Model):
    full_name = models.CharField(max_length= 100)
    short_name = models.CharField(max_length =10)
    year_of_esht = models.CharField(max_length =4)
    num_of_seats = models.IntegerField()
    is_ugc_accre = models.BooleanField(default= False)
    is_nb_accre = models.BooleanField(default= False)
    departments = models.ManyToManyField(core_models.Department,related_name="program_department")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Programs"

class Course(models.Model):
    course_code = models.CharField(max_length = 50,null= True)
    subject = models.CharField(max_length= 100,null =True)
    credit = models.IntegerField()
    contact_hours = models.IntegerField()
    course_type = models.CharField(choices = COURSE_TYPE_CHOICES,max_length=50,null = True)
    department = models.ForeignKey(core_models.Department,related_name='course_department',on_delete=models.CASCADE,null = True)
    def __str__(self):
        return self.course_code
    class Meta:
        verbose_name_plural= "Courses"

class SemesterCourse(models.Model):
    sem_record = models.ForeignKey('SemesterRecord',on_delete = models.CASCADE, null =True)
    course = models.ForeignKey(Course,related_name='sem_coursedetails',on_delete=models.CASCADE,null = True)
    faculty =models.ForeignKey(faculty_models.Faculty,related_name='semcourse_fcltydetails',on_delete=models.CASCADE,null = True)
    daily_class_report = models.ManyToManyField('DailyClassReport',related_name= 'sem_course_daily_class_report')

    class Meta:
        verbose_name_plural = "SemesterCourses"
class SemesterRecord(models.Model):
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    student = models.ManyToManyField(to='student.Student',related_name="sem_rec_studentdetail")
    sem_course = models.ManyToManyField(SemesterCourse,related_name="sem_rec_sem_coursedetail")
    sem_type = models.CharField(max_length=10,choices=SEMESTER_CHOICES,null =True)
    dept = models.ForeignKey(core_models.Department,on_delete=models.CASCADE,null = True)

    def __str__(self):
        return self.sem_course.course.subject + "_" +self.start_date
    
    class Meta:
        verbose_name_plural ="SemesterRecords"

class Examination(models.Model):
    sem_rec = models.ForeignKey(SemesterRecord,related_name='exam_semrecdeetails',on_delete =models.CASCADE,null = True)
    sem_course = models.ForeignKey(SemesterCourse,related_name='exam_semcoursedetails',on_delete=models.CASCADE,null = True)
    total_marks = models.IntegerField()
    exam_type = models.CharField(max_length=50,choices=EXAMINATION_CHOICES,default = "ENDSEM")
    dept = models.ForeignKey(core_models.Department, related_name= 'Exam_deptdetail',on_delete=models.CASCADE,null= True)

    class Meta:
        verbose_name_plural = "Examinations"


class DailyClassReport(models.Model):
    sem_course = models.ForeignKey(SemesterCourse,related_name='clsrpt_semcoursedetails',on_delete= models.CASCADE,null = True)
    class_date = models.DateField(null=True)
    class_time = models.TimeField(null= True)
    faculty = models.ForeignKey(faculty_models.Faculty,related_name='clsrpt_fcltydetails',on_delete=models.CASCADE,null = True)
    student_prsnt = models.ManyToManyField(student_models.Student,related_name="clsrpt_Studentdetail")
    topics_cover = models.IntegerField()

    def __str__(self):
        return self.sem_course.course.subject + '_' +self.topics_cover

    class Meta:
        verbose_name_plural = 'DailyClassReports'

class SemesterMarks(models.Model):
    student = models.OneToOneField(student_models.Student,on_delete=models.SET_NULL,null=True)
    sem_course = models.ForeignKey(SemesterCourse,on_delete=models.CASCADE,related_name='semmark_coursedetails',null = True)
    total_marks = models.IntegerField()
    marks_obtained = models.IntegerField()
    exam = models.OneToOneField(Examination,on_delete = models.CASCADE,null=True)
    faculty = models.ForeignKey(faculty_models.Faculty,related_name='semmarks_fcltydetails',on_delete=models.CASCADE,null = True)
    department = models.ForeignKey(core_models.Department,related_name="semmarks_deptdetails", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural= 'SemesterMarks'