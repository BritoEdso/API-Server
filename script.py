import requests

query_params = {"offset": 2, "limit": 2, "max_price": 40}
response = requests.get(
    "http://127.0.0.1:8000/api/items",
    params=query_params,
)
print(response.json())