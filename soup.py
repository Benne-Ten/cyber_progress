from bs4 import BeautifulSoup


html = """
<html>
  <body>
    <div class="article">
      <h2>Python Tips</h2>
      <p>Learn Python in 10 days</p>
    </div>
    <div class="article">
      <h2>Web Scraping</h2>
      <p>Scrape websites ethically</p>
    </div>
  </body>
</html>
"""
search = BeautifulSoup(html, 'html.parser')

result = search.find_all(['h2', 'p'])
for elem in result:
	print(elem.text)
