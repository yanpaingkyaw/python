import os
import yagmail
from pathlib import Path

DEBUG = True

DEBUG_IPS = ['1.1.1.1', '8.8.8.8', '127.0.0.1']

if DEBUG:
    ips = DEBUG_IPS
else:
    with open("IPs.txt", "r+") as ips_file:
        ips = [ip.strip() for ip in ips_file.readlines()]

with open("IPsCheck.txt", "w") as available_ips_file:
    for ip in ips:
        response = os.system('ping {}'.format(ip))
        if response == 0:
            result = ip + ':OK' + ' \n'
            available_ips_file.write(result)
        else:
            print('server {} not available'.format(ip))
            available_ips_file.write('server {} not available\n'.format(ip))


#initializing the server connection
yag = yagmail.SMTP(user='hanaict2020@gmail.com', password='@dmin123')
#sending the email
filename = 'IPsCheck.txt'
yag.send(to=' yanpk@hanamicrofinance.com', subject='InternetChecking', contents='Please find the image attached', attachments=filename)
print('Email sent successfully')
