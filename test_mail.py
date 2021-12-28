from django.core.mail import BadHeaderError, send_mail
from django.conf import Settings

send_mail('Testing this', 'testing the email from vssut email', 'fa_enigma@vssut.ac.in', ['priyanshusingh1998@gmail.com', 'aitik2000@gmail.com'])



