import requests
import logging
from requests.adapters import HTTPAdapter
from urllib3 import Retry

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.DEBUG)

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    with requests.Session() as s:
        retries = Retry(connect=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retries)
        s.mount('http://', adapter)
        s.mount('https://', adapter)

        try:
            response = s.get(url)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as err:
            return f"Error occurred: {err}"

# Example usage:
if __name__ == "__main__":
    posts = fetch_posts()
    print(posts)
