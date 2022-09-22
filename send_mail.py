import json
import pandas as pd
import os
import sys
import smtplib
from datetime import date
import psycopg2
import boto3
# from tabulate import tabulate
import numpy as np
from prettytable import PrettyTable
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail_reports(attachments=[], recipients=[], tabular_table=None, tabular_table_1=None, ccrecipients=[],
                      **kwargs):
    today = str(date.today()).replace('-', '_')
    # sender = 'ops.eregistry@gmail.com'
    sender = 'ops.eregistry@dvara.com'
    gmail_password = 'Welcome@2021'  # 'Dvara@2021'

    COMMASPACE = ', '
    # recipients = ['eswar.m@dvara.com', 'Deepak.Singhal@Dvara.com'  ]

    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = 'Doordrishti Fin MIS-' + today
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'
    # List of attachments
    # att = '/home/ubuntu/workspace/FRMIS/'+today+'_InputAnalytics.xlsx'
    # att = today+'_InputAnalytics.xlsx'

    # attachments = [att]

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    my_message = 'tabular_table.get_html_string()'
    my_message_1 = 'tabular_table_1.get_html_string()'

    text = "Hi!"

    html = """\
    <html>
        <head>
        <style>
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
            }
            th, td {
                padding: 5px;
                text-align: left;    
            }    
        </style>
        </head>
    <body>
    <p>Farmer Summary Details Monthly<br>

       %s
    </p>
    <br>
    <br>
    <p>Farmer Summary Details<br>

       %s
    </p>  
    </body>
    </html>
    """ % (my_message_1, my_message)

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    email_body = MIMEMultipart("alternative", None, [part1, part2])

    # if kwargs['body']:
    #    email_body=email_body+kwargs['body']
    # body = MIMEText(email_body, 'plain')

    outer.attach(email_body)
    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.office365.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
        msg = 'Mail Send Successfully'
        return True, msg
    except Exception as e:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        msg = 'Mail Not Send Successfully. Error: ", {}'.format(e)
        return False, msg
    # return "Mail Send Successfully"

attachments= []
to_recipients = ['teja.yangala@dvara.com']
cc_recipients = []
tabular_table = ''
tabular_table_1 = ''
mail_sent, mail_response = send_mail_reports(attachments, to_recipients, tabular_table=tabular_table,
                                                 tabular_table_1=tabular_table_1, ccrecipients=cc_recipients)

def send_mail_reports_1(recipients=[]):
    today = str(date.today()).replace('-', '_')
    sender = 'ops.eregistry@dvara.com'
    password = 'Welcome@2021'  # 'Dvara@2021'

    COMMASPACE = ', '

    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = 'Testing ' + today
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    text = "Hi!"

    part1 = MIMEText(text, 'plain')
    # part2 = MIMEText(html, 'html')
    email_body = MIMEMultipart("alternative", None, [part1])
    outer.attach(email_body)
    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.office365.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, password)
            s.sendmail(sender, recipients, composed)
            s.close()
    except Exception as e:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise e
    return 'Mail sent Successfully'


if __name__ == "__main__":
    send_mail_reports_1(recipients=["vinodkumar.t@dvara.com"])
    mail_sent, mail_response = send_mail_reports(attachments, to_recipients, tabular_table=tabular_table,
                                                 tabular_table_1=tabular_table_1, ccrecipients=cc_recipients)
