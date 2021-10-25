import email
from email.mime import text
from os import read
import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_sender = #"Your email here"
password = #"your email's password here"
subject = #"subject of email"

with open(#path to your file, 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        what_to_send = #Your message goes here. Eg: "Hi " + line[0] + "/n" + "How are you?"
        person = line[1] #person is the receiver's email address and line[1] is the index of where the email is in the CSV
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = person
        msg['Subject'] = subject
        msg.attach(MIMEText(what_to_send, "plain"))
        what_to_send = msg.as_string()

        server = smtplib.SMTP_SSL("", ) #enter the email server and the port
        server.login("", "")#enter your email and password
        server.sendmail(email_sender, person, what_to_send)

        server.quit()


#NOTE: Make sure that your CSV has no headers.


