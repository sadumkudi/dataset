import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

class CountingHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.retry_count = 0

    def send(self, request, **kwargs):
        response = super().send(request, **kwargs)
        self.retry_count += 1
        return response

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    with requests.Session() as s:
        retries = Retry(connect=3, backoff_factor=0.5)
        adapter = CountingHTTPAdapter(max_retries=retries)
        s.mount('http://', adapter)
        s.mount('https://', adapter)

        try:
            response = s.get(url)
            response.raise_for_status()
            print(f"Number of attempts: {adapter.retry_count}")
            return response.json()

        except requests.exceptions.RequestException as err:
            return f"Error occurred: {err}, Number of attempts: {adapter.retry_count}"

# Example usage:
if __name__ == "__main__":
    posts = fetch_posts()
    print(posts)
