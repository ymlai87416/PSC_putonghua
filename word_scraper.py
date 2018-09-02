# 词语表（表一) http://www.pthxx.com/b_audio/03_zici_1/index.html
# 词语表（表二) http://www.pthxx.com/b_audio/04_zici_2/001.html

# 作品 1-60 號 http://yueputang.org/yueputang.org/wp-content/uploads/2016/02/psc60.pdf
import pandas as pd
from pandas import Series, DataFrame

from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import json
import csv
import requests
import lxml

def word_one_url_generator:
	template = "http://www.pthxx.com/b_audio/03_zici_1/%02d.html"
	max_pg =66
	for i in range(1, max_pg+1):
		yield template % i
	
def word_two_url_generator:
	template = "http://www.pthxx.com/b_audio/04_zici_2/%03d.html"
	max_pg =105
	for i in range(1, max_pg+1):
		yield template % i

def extract_word_list(url):
	result = requests.get(url)
	c= result.content
	soup = BeautifulSoup((c), "lxml")

	soup.prettify()

	summary = soup.find('table',attrs = {'class':'tablehead'})
	tables = summary.find_all('div')

	#tables = summary.fins_all('td' /'tr')

	data =[]

	rows = tables[0].findAll('tr')
	soup = BeautifulSoup((html), "lxml")
	table = soup.find('table', attrs = {'class' : 'tablehead'})

	list_of_rows=[]

	for row in table.findAll('tr')[0:]:
	list_of_cells=[]
	for cell in findAll('td'):
	text = cell.text.replace(' ','')
	list_of_cells.append(text)
	list_of_rows.append(list_of_cells)

	print(list_of_rows)
	return list_of_rows

def build_word_one_list:
	pass
	
def build_word_two_list:
	pass
	


