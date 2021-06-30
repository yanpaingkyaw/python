import smtplib
import os
import time
from email.message import EmailMessage

### Pinging ###
file = open('logfile.txt','w+')
print('127.0.0.1 is being pinging...')
response=os.popen(f"ping 127.0.0.1").read()
file.write(str(response))
file.close()
time.sleep(2)
print('Pinging 127.0.0.1 Finished!')
#### Finished Pinging and logfile saving ###

user='eieinyeinchan@mahaawba.com'
password='Nyein0828'
smtpsrv="smtp.office365.com"
smtpserver=smtplib.SMTP(smtpsrv,587)

### Creating email structure ###
msg=EmailMessage()
msg['Subject']='Email Testing with Python'
msg['From']='eieinyeinchan@mahaawba.com'
msg['To']='mahait@mahaawba.com'

with open('logfile.txt') as f:
    msg.set_content(f.read())

time.sleep(2)
print('Sending mail...')
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(user,password)
smtpserver.send_message(msg)
time.sleep(2)
print('Mail sent!!!')
smtpserver.close()
