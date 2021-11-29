from django.db import models 
from django.conf import settings
from django.db.models.deletion import SET_DEFAULT
from core.models import User
from django_countries.fields import CountryField
from core.models import Branch
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from core.models import Branch

ENTRANCE_CHOICES = (
    ('JEE-MAIN', 'JEE-MAIN'),
    ('OJEE', 'OJEE')
)

PROGRAMME_CHOICES = (
    ('B.Tech.','B.Tech.'),
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

TFW_CHOICES = (
    ("YES","YES"),
    ("NO","NO")
)

MODE_CHOICES = (
    ("REGULAR","REGULAR"),
    ("SELF-SUSTAINING","SELF-SUSTAINING")
)

PWD_CHOICES = (
    ("YES","YES"),
    ("NO","NO")
)

DEFENCE_CHOICES = (
    ("YES","YES"),
    ("NO","NO")
)

GREENCARD_CHOICES = (
    ("YES","YES"),
    ("NO","NO")
)

# class Employee(models.Model):
#     #eid=models.CharField(max_length=20)
#     fname=models.CharField(max_length=100)
#     mname=models.CharField(max_length=100)
#     lname=models.CharField(max_length=100)
#     jeeroll=models.CharField(max_length=100)
#     jeerank=models.CharField(max_length=100)
#     egate=models.CharField(max_length=15, choices=EGATE_CHOICES)
#     programme=models.CharField(max_length=50,choices=PROGRAMME_CHOICES)
#     branch=models.CharField(max_length=50,choices=BRANCH_CHOICES)
#     days=models.CharField(max_length=50,choices=DAY_CHOICES)
#     month=models.CharField(max_length=50,choices=MONTH_CHOICES)
#     year=models.CharField(max_length=50,choices=YEAR_CHOICES)
#     country= CountryField()
#     religion = models.CharField(max_length=50,choices=RELIGION_CHOICES)
#     blood = models.CharField(max_length=5,choices=BLOOD_CHOICES)
#     tfw = models.CharField(max_length=5,choices=TFW_CHOICES)
#     mode = models.CharField(max_length=20,choices=MODE_CHOCES)
#     pwd = models.CharField(max_length=5,choices=PWD_CHOICES)
#     defence = models.CharField(max_length=3,choices=DEFENCE_CHOICES)
#     greencard = models.CharField(max_length=5,choices=GREENCARD_CHOICES)
#     fathername=models.CharField(max_length=100)
#     mothername=models.CharField(max_length=100)
#     eemail=models.EmailField()
#     econtact=models.CharField(max_length=15)
#     gemail=models.EmailField()
#     gcontact=models.CharField(max_length=15)
#     tenclg=models.CharField(max_length=15)
#     tenboard=models.CharField(max_length=15)
#     tentotalcgpa=models.CharField(max_length=15)
#     tenseccgpa=models.CharField(max_length=15)
#     tenpercentage=models.CharField(max_length=15)
#     tenyop=models.CharField(max_length=15)
#     twelveclg=models.CharField(max_length=15)
#     twelveboard=models.CharField(max_length=15)
#     twelvetotalcgpa=models.CharField(max_length=15)
#     twelveseccgpa=models.CharField(max_length=15)
#     twelvepercentage=models.CharField(max_length=15)
#     twelveyop=models.CharField(max_length=15)
#     is_valid = models.BooleanField(default=False)


#     class Meta:
#         db_table="employee"

#     def __str__(self):
#         return self.fname + ' ' + self.mname + ' ' + self.lname



class Student_Application(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    jee_roll = models.CharField(max_length=100, null=True)
    jee_rank = models.CharField(max_length=100, null=True)
    programme = models.CharField(max_length=50,choices=PROGRAMME_CHOICES, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    #academic_session = models.CharField(max_length=50,choices=(2021,)),
    entrance_exam = models.CharField(max_length=50,choices=ENTRANCE_CHOICES),
    is_Tfw = models.BooleanField(default=False),
    mode = models.CharField(max_length=50,choices=MODE_CHOICES),
    is_pwd = models.BooleanField(default=False),
    is_defence = models.BooleanField(default=False),
    is_green_card = models.BooleanField(default=False),
    parents_mobile = models.CharField(max_length=11),
    parents_email = models.CharField(max_length=100),
    application_time = models.DateTimeField(),
    status = models.BooleanField(),


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
    application = models.OneToOneField('Student_Application', on_delete=models.CASCADE),
    verification_time = models.DateTimeField()


    #verify this
    verified_by = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=SET_DEFAULT,default='Admin')








    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name + '-' + self.last_name)
        slug_eixts = Student.objects.filter(slug=self.slug).exists()
        if slug_eixts:
            self.slug += '-' + str(self.user.id)
        
        super(Student, self).save(*args, **kwargs)
