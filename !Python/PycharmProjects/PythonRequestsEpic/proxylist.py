import requests
from bs4 import BeautifulSoup
import tabulate
import csv

html = requests.get('https://www.free-proxy-list.net/')
content = BeautifulSoup(html.text, 'lxml')
table = content.find('table')
rows = table.findAll('tr')

print(rows[0])
