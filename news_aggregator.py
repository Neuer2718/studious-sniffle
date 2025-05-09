import requests

API_KEY = "API_KEY"
URL = "https://newsapi.org/v2/top-headlines"

def get_headlines(country='us', category='technology'):
    params = {
        'apiKey': API_KEY,
        'country': country,
        'category': category,
        'pageSize': 5,
    }

    response = requests.get(URL, params=params)
    data = response.json()

    for article in data['articles']:
        print(f"Title: {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"URL: {article['url']}\n")

get_headlines()