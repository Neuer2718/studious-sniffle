import requests

# NewsAPI key (replace with your own key)
API_KEY = "API_KEY"
URL = "https://newsapi.org/v2/top-headlines"

# Function to fetch and display headlines
def get_headlines(country='us', category='technology'):
    # Set up request parameters
    params = {
        'apiKey': API_KEY,
        'country': country,
        'category': category,
        'pageSize': 5,
    }

    # Make GET request to NewsAPI
    response = requests.get(URL, params=params)
    
    # Parse the JSON response
    data = response.json()

    # Loop through each article
    for article in data['articles']:
        print(f"Title: {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"URL: {article['url']}\n")

# Call the function with user-provided values
get_headlines()
