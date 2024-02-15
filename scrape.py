import requests
import pandas as pd

# Define your API key and search engine ID
API_KEY = 'AIzaSyBrxAa_pt4h8rkmJ3JvR6sXadyEeTrW1Fw'
SEARCH_ENGINE_ID = 'd3b927a5d95364c54'

def google_search(query):
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&num=10"
    response = requests.get(url)
    data = response.json()
    return data.get('items', [])

def extract_data(word):
    results = google_search(word)
    extracted_data = []
    for result in results:
        item = {
            'title': result.get('title', ''),
            'link': result.get('link', ''),
            'snippet': result.get('snippet', ''),
            'source': result.get('displayLink', '')
        }
        extracted_data.append(item)
    return extracted_data

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    word = "Canoo"
    data = extract_data(word)
    save_to_csv(data, f"{word}_search_results.csv")
