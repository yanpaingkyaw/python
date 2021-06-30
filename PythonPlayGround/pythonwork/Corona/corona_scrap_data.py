import requests
import csv
from bs4 import BeautifulSoup

f = csv.writer(open('corona_data.csv', 'w'))
f.writerow(['World Corona Virus Situtation Data'])
f.writerow(['----------------------------------'])

x = requests.get('https://ncov2019.live/')
print(x.status_code)
soup = BeautifulSoup(x.text, 'html.parser')


tag = soup.find(lambda tag: tag.name == 'div' and tag['class'] == ['container--wrap'])
data_list_items = tag.find_all('p')

label_list = ['confirmed case:', 'Total Decased:', 'Total Serious:', 'Total Recovered:']
for items in data_list_items:
    data = items.contents[0]
    if data.strip() != 'Quick Facts' and data.strip() != 'updated:' and data.strip() != 'Total Confirmed Cases' and data.strip() != 'Total Deceased' and data.strip() != 'Total Serious' and data.strip() != 'Total Recovered':
        for i in range(0,3):
            if i == 0:
                print(label_list[0], data.strip())  
                break
            elif i==1:
                print(label_list[1], data.strip())
                break
            elif i==2:
                print(label_list[2], data.strip())
                break
            else:
                print(label_list[3], data.strip())
                break
            #f.writerow([data.strip()])
print('Successfully created csv file!')

