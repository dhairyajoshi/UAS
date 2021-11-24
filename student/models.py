from django.db import models 

from django.contrib.auth.models import User
from django_countries.fields import CountryField
from core.models import Branch

EGATE_CHOICES = (
    ('JEE-MAIN', 'JEE-MAIN'),
    ('OJEE', 'OJEE')
)

PROGRAMME_CHOICES = (
    ('B.Tech.','B.Tech.'),
)

BRANCH_CHOICES = (
    ('Chemical Engineering','Chemical Engineering'),
    ('Civil Engineering','Civil Engineering'),
    ('Computer Science & Engineering','Computer Science & Engineering'),
    ('Electrical Engineering','Electrical Engineering'),
    ('Electrical & Electronics Engineering','Electrical & Electronics Engineering'),
    ('Electronics & Telecomm. Engineering','Electronics & Telecomm. Engineering'),
    ('Information Technology','Information Technology'),
    ('Mechanical Engineering','Mechanical Engineering'),
    ('Metallurgical & Materials Engineering','Metallurgical & Materials Engineering'),
    ('Production Engineering','Production Engineering')
)
DAY_CHOICES=()
for i in range(1,32):
    y=(str(i),str(i)),
    DAY_CHOICES+=y

MONTH_CHOICES=(
    ('JAN','JAN'),
    ('FEB','FEB'),
    ('MAR','MAR'),
    ('APR','APR'),
    ('MAY','MAY'),
    ('JUN','JUN'),
    ('JULY','JULY'),
    ('AUG','AUG'),
    ('SEP','SEP'),
    ('OCT','OCT'),
    ('NOV','NOV'),
    ('DEC','DEC')
)
YEAR_CHOICES=()
for i in range(1950,2011):
    y=(str(i),str(i)),
    YEAR_CHOICES+=y

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

MODE_CHOCES = (
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



class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    jeeroll=models.CharField(max_length=100)
    jeerank=models.CharField(max_length=100)
    egate=models.CharField(max_length=15, choices=EGATE_CHOICES)
    programme=models.CharField(max_length=50,choices=PROGRAMME_CHOICES)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    days=models.CharField(max_length=50,choices=DAY_CHOICES)
    month=models.CharField(max_length=50,choices=MONTH_CHOICES)
    year=models.CharField(max_length=50,choices=YEAR_CHOICES)
    country= CountryField()
    religion = models.CharField(max_length=50,choices=RELIGION_CHOICES)
    blood = models.CharField(max_length=5,choices=BLOOD_CHOICES)
    tfw = models.CharField(max_length=5,choices=TFW_CHOICES)
    mode = models.CharField(max_length=20,choices=MODE_CHOCES)
    pwd = models.CharField(max_length=5,choices=PWD_CHOICES)
    defence = models.CharField(max_length=3,choices=DEFENCE_CHOICES)
    greencard = models.CharField(max_length=5,choices=GREENCARD_CHOICES)
    fathername=models.CharField(max_length=100)
    mothername=models.CharField(max_length=100)
    eemail=models.EmailField()
    econtact=models.CharField(max_length=15)
    gemail=models.EmailField()
    gcontact=models.CharField(max_length=15)
    tenclg=models.CharField(max_length=15)
    tenboard=models.CharField(max_length=15)
    tentotalcgpa=models.CharField(max_length=15)
    tenseccgpa=models.CharField(max_length=15)
    tenpercentage=models.CharField(max_length=15)
    tenyop=models.CharField(max_length=15)
    twelveclg=models.CharField(max_length=15)
    twelveboard=models.CharField(max_length=15)
    twelvetotalcgpa=models.CharField(max_length=15)
    twelveseccgpa=models.CharField(max_length=15)
    twelvepercentage=models.CharField(max_length=15)
    twelveyop=models.CharField(max_length=15)
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
