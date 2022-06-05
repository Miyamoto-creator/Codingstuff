import requests
from bs4 import BeautifulSoup
from tabulate import *
import csv

html = requests.get('https://www.free-proxy-list.net/')
content = BeautifulSoup(html.text, 'lxml')
table = content.find('table')
rows = table.findAll('tr')
headers = [header.text for header in rows[0]]
results = [headers]

for row in rows:
    if len(row.findAll('td')):
        results.append([data.text for data in row.findAll('td')])
print(tabulate(results, headers, tablefmt='fancy_grid'))

with open('proxies.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(results)
