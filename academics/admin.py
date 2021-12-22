from django.contrib import admin
from .models import Program,Course,SemesterCourse,SemesterRecord,SemesterMarks,DailyClassReport,Examination

# Register your models here.
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(SemesterCourse)
admin.site.register(SemesterRecord)
admin.site.register(SemesterMarks)
admin.site.register(DailyClassReport)
admin.site.register(Examination)