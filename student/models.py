from django.db import models 
from django.conf import settings
from django.db.models.deletion import SET_DEFAULT
from django_countries.fields import CountryField
from core.models import Department,Program
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify



ENTRANCE_CHOICES = (
    ('JEE-MAIN', 'JEE-MAIN'),
    ('OJEE', 'OJEE')
)

PROGRAMME_CHOICES = (
    ('B.Tech.','B.Tech.'),
    ('B.Tech. DD.','B.Tech. + M.Tech.'),
    ('M.Tech.','M.Tech.'),
    ('B.Arch.','B.Arch.'),
    ('MCA','MCA'),
    ('M.Sc.','M.Sc'),
    ('Int.M.Sc','Int.M.Sc'),
    ('M.Phil.','M.Phil.'),
    ('Ph.D.','Ph.D')
)

RELIGION_CHOICES = (
    ("HINDU","HINDU"),
    ("CHRISTIAN","CHRISTIAN"),
    ("MUSLIM","MUSLIM"),
    ("SIKH","SIKH"),
    ("JAIN","JAIN"),
    ("PARSI","PARSI"),
    ("BUDDHIST","BUDDHIST"),
    ("JEWISH","JEWISH"),
    ("JEWSIH","JEWISH")
)


BLOOD_CHOICES = (
    ("A+","A+"),
    ("B+","B+"),
    ("AB+","AB+"),
    ("O+","O+"),
    ("A-","A-"),
    ("B-","B-"),
    ("AB-","AB-"),
    ("O-","O-")
)


MODE_CHOICES = (
    ("REGULAR","REGULAR"),
    ("SELF-SUSTAINING","SELF-SUSTAINING")
)


class Student_Application(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE,null= True)
    course = models.ManyToManyField(Program,related_name='student_applicant_courses')
    jee_roll = models.CharField(max_length=100, null=True)
    jee_rank = models.CharField(max_length=100, null=True)
    programme = models.CharField(max_length=50,choices=PROGRAMME_CHOICES, null=True)
    #academic_session = models.CharField(max_length=50,choices=(2021,)),
    entrance_exam = models.CharField(max_length=50,choices=ENTRANCE_CHOICES,default = "JEE-MAIN")
    is_Tfw = models.BooleanField(default = False)
    mode = models.CharField(max_length=50,choices=MODE_CHOICES,default= "REGULAR")
    is_pwd = models.BooleanField(default=False)
    is_defence = models.BooleanField(default=False)
    is_green_card = models.BooleanField(default=False)
    parents_mobile = models.CharField(max_length=12,null = True)
    parents_email = models.EmailField(null= True)
    application_time = models.DateTimeField(null = True)
    status = models.BooleanField(default=False)

    slug = models.SlugField(unique= True,blank=True)
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.first_name + '-' + self.last_name)
        slug_eixts = Student_Application.objects.filter(slug=self.slug).exists()
        if slug_eixts:
            self.slug += '-' + str(self.user.id)
        
        super(Student_Application, self).save(*args, **kwargs)


class Student(models.Model):
    registration =models.BigIntegerField(unique=True,null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    application = models.OneToOneField(Student_Application, on_delete=models.CASCADE,null =True)
    verification_time = models.DateTimeField(null =True)
    verified_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='student_verifier', on_delete=models.SET_NULL, null=True)
    dept = models.ForeignKey(Department,on_delete = models.CASCADE,null= True)
    course = models.ForeignKey(Program,on_delete = models.CASCADE,null=True)
    entrance_exam = models.CharField(max_length = 50,choices=ENTRANCE_CHOICES,default= "JEE-MAIN")
    academic_session= models.CharField(max_length=5,null=True)
    is_tfw = models.BooleanField(default=False)
    mode = models.CharField(max_length=50,choices=MODE_CHOICES,default="REGULAR")
    is_pwd = models.BooleanField(default=False)
    is_defence = models.BooleanField(default=False)
    is_green_card = models.BooleanField(default=False)
    parent_email = models.EmailField(null= True)
    parent_mobile = models.CharField(max_length=12,null=True)
    jee_roll = models.CharField(max_length=50,null=True)
    jee_rank = models.CharField(max_length=50,null=True)
    entry_gate = models.CharField(max_length= 50,null=True)
    program = models.CharField(max_length=50,choices = PROGRAMME_CHOICES,null= True)
    application_time = models.DateTimeField(null= True)
    status = models.BooleanField(default = False)

    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        unique_together = (("registration"),)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name + '-' + self.last_name)
        slug_eixts = Student.objects.filter(slug=self.slug).exists()
        if slug_eixts:
            self.slug += '-' + str(self.user.id)
        
        super(Student, self).save(*args, **kwargs)
