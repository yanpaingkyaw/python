import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'hanaict2020@gmail.com'
EMAIL_PASSWORD = '@dmin123'

msg = EmailMessage()
msg['Subject'] = 'Testing attachment'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'yanpaingkyaw@gmail.com'
msg.set_content('Pls refer to the attachment')

files = ['test_attachment.txt']
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
