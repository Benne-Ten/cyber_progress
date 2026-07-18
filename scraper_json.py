import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts?userId=1')
posts = response.json()  # C'est une liste

for post in posts:
    print(f"Titre: {post['title']}")
    print(f"Body: {post['body']}")
    print("\n")
