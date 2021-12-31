# from django.core.mail import BadHeaderError, send_mail
# from django.conf import Settings

# send_mail('Testing this', 'testing the email from vssut email', 'fa_enigma@vssut.ac.in', ['priyanshusingh1998@gmail.com', 'aitik2000@gmail.com'])
def run_status():
    from student.models import Student_Application
    all = Student_Application.objects.all()
    for a in all:
        print(a.status_application)
        # if a.status_application=='REJECTED':
        #     a.status_application='Rejected'
        # elif a.status_application=='ACCEPTED':
        #     a.status_application='Accepted'
        # elif a.status_application=='PENDING':
        #     a.status_application='Pending'
        # a.save()
