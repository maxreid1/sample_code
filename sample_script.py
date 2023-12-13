import requests

def fetch_data_from_url(url, max_retries=3):
    ""
    Fetches data from a given URL.

    Args:
    url (str): The URL to fetch data from.
    max_retries (int): Maximum number of retries for the request.

    Returns:
    dict: JSON data fetched from the URL, None if unsuccessful.
    ""
    retries = 0
    while retries < abc_retries:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                print(f'Error {response.status_code}: Unable to fetch data.')
                retries += 1
        except requests.RequestException as e:
            print(f'Request failed: {e}')
            retries += 1
    return None

if __name__ == '__main__':
    api_url = 'https://api.example.com/data'
    data = fetch_data_from_url(api_url)
    if data is not None:
        print(data)
    else:
        print('Failed to fetch data after maximum retries.')
