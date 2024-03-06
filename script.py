import requests

try:
    response = requests.get("http://127.0.0.1:8000/api/cock")
    response.raise_for_status()
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occured: {http_err}")
except Exception as err:
    print(err)
else:
    print(response.status_code)