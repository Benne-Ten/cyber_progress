from bs4 import BeautifulSoup

html = """
<div id="posts">
  <article class="post" data-id="1">
    <h3>Post 1</h3>
    <p class="meta">By Alice</p>
  </article>
  <article class="post" data-id="2">
    <h3>Post 2</h3>
    <p class="meta">By Bob</p>
  </article>
</div>
"""

soup = BeautifulSoup(html, 'html.parser')

result = soup.find_all('article')
for article in result:
	h3_result = article.find('h3')
	print(h3_result.text) 
	meta_result = article.find('p', class_='meta')
	print(meta_result.text)
	data_result = article.get('data-id')
	print(data_result, "\n")
