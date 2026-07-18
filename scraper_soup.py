from bs4 import BeautifulSoup
import requests


url = 'https://example.com'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


h_result = soup.find_all(['h1', 'h2', 'h3'])
for element in h_result:
	print(element.text)
p_result = soup.find_all('p')
for element in p_result:
	print(element.text)
link_result = soup.find_all('a')
for element in link_result:
	print(element.get('href'))

