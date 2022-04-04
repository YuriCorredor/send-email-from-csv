import smtplib
import os
import re
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import csv

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TITLE = os.getenv("TITLE")

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

print("Written by Yuri Corredor")

html_body = ""
with open("body.html", "r", encoding='utf-8') as f:
    html_body = f.read()

def main(csv_file):
    reader = csv_reader(csv_file)
    send_emails(reader)

def isValidEmail(email):
    if re.fullmatch(regex, email):
        return True
    return False

def send_emails(emails):
    for row in emails:
        try:
            email = row[0]
            isValid = isValidEmail(email)
        except Exception as exception:
            print(exception)
        if email and isValid:
            send_email_to(email)
            print('Email enviado para "{}"!'.format(email))

def csv_reader(file_name):
    f = open(file_name, 'r')
    reader = csv.reader(f)
    return reader

def attach_files(message, files_names):
    for name in files_names:
        with open(f"{path}/attachment/{name}", 'rb') as file:
            payload = MIMEApplication(file.read(), name=name)
            payload.add_header('content-decomposition', 'attachment; filename={}'.format(name))
            message.attach(payload)

def send_email_to(receiver):
   
    content = html_body

    message = MIMEMultipart()
    message['From'] = EMAIL
    message['To'] = receiver

    message['Subject'] = TITLE

    message.attach(MIMEText(content, 'html'))
    
    files_to_attach = [f for f in os.listdir(f"{path}/attachment")]
    if files_to_attach: attach_files(message, files_to_attach)

    message_to_send = message.as_string()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, receiver, message_to_send)
    except Exception as exception:
        try:
            server.connect()
            print(exception)
        except Exception as exception:
            send_email_to(receiver)
            print(exception)

path = os.path.dirname(os.path.realpath(__file__))
csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
for csv_file in csv_files:
    print(f"Reading {csv_file}...")
    main(csv_file)