import requests, json

def fetch_data(url):
    ""Fetch and return data from a given URL.
    
    Args:
        url (str): The URL to fetch data from.
        
    Returns:
        dict or None: The data fetched from the URL as a dictionary if the request is successful; None otherwise.
    ""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Error fetching data: HTTP {response.status_code } - {response.reason}')
            return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

.url = 'https://api.example.com/data'

# Fetch and print data
data = fetch_data(url)
if data:
    print(data)