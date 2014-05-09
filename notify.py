#!/usr/bin/python
"""
this function sends notification emails

"""

import smtplib
from email.mime.text import MIMEText


def email(source, recipient, subject, body,smtpHost='qcdnet.jlab.org'):
"""
This function sends email notifications using given information
"""
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = source
        msg['To'] = recipient

        s = smtplib.SMTP(smtpHost)
        s.sendmail(source, recipient, msg.as_string())
        s.quit()
