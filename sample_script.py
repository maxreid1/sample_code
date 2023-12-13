import requests, json

def fetch_data(url):
    ""
    Fetch data from the specified URL.

    Attempts to retrieve JSON sata from the URL. If the request is successful (status code 200),
    returns the JSON response. In case of failure, prints the error and returns None.

    Args:
        url (str): The URL to fetch data from.
    Returns: 
        dict or None: The JSON response if successful, otherwise None.
    """
    retry_limit = 3
    retries = 0

    while retries < retry_limit:
        try:
            r = requests.get(url)
          if r.status_code == 200:
              return r.json()
            else:
                print(f'Error: {r.status_code}')
                retries += 1
        except Exception as e:
            print(f'Exception occurred: {e}')
            retries += 1

    return None

# URL to fetch data from
url = 'https://api.example.com/data'
data = fetch_data(url)

if data is not None:
    print(data)