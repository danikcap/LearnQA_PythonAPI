import requests
import json
import time

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
text = json.loads(response1.text)
print(text)
token1 = text["token"]
t = text["seconds"]

response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token1})
text2 = json.loads(response2.text)
print(text2)
status = text2["status"]
assert status == "Job is NOT ready"

time.sleep(t)
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token1})
text3 = json.loads(response3.text)
print(text3)
status = text3["status"]
assert status == "Job is ready"
assert text3.get("result")


