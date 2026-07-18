from bs4 import BeautifulSoup
import requests

url = 'https://jsonplaceholder.typicode.com/'
response = requests.get(url)


html = BeautifulSoup(response.text, 'html.parser')

result = html.find_all('a')
for elem in result:
        print(elem.get('href'))
