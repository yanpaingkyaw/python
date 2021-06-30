import requests
import csv
from bs4 import BeautifulSoup

f = csv.writer(open('data.csv', 'w'))
f.writerow(['Name', 'Link'])

x = requests.get('http://web.mta.info/developers/turnstile.html')
print(x.status_code)
soup = BeautifulSoup(x.text, 'html.parser')
data_list = soup.find(class_='span-84 last')
data_list_items = data_list.find_all('a')

for data in data_list_items:
    name = data.contents[0]
    link = data.get('href')
    print(name, link)
    f.writerow([name, link])

print('total record:', len(data_list_items))    