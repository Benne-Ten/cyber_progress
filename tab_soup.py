from bs4 import BeautifulSoup


html = """
<table>
  <tr>
    <th>Nom</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Alice</td>
    <td>25</td>
  </tr>
  <tr>
    <td>Bob</td>
    <td>30</td>
  </tr>
</table>
"""

soup = BeautifulSoup(html, 'html.parser')
result = soup.find_all('td')
for i in range(0, len(result), 2):
	print(f'{result[i].text} : {result[i+1].text}')
