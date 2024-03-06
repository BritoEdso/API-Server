import requests

def log_url(response, *args, **kwargs):
    print(f"Requested URL: {response.url}")

response = requests.get(
    "http://127.0.0.1:8000/api/items",
    hooks={"response": log_url},
)