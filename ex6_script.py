import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

for resp in response.history:
    print(resp.url)
print(response.url)
