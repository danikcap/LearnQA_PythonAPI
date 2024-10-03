import requests

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response1.text)
print("==============")

response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "HEAD"})
print(response2.text)
print("==============")

response3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
print(response3.text)
print("==============")

methods = {"GET": requests.get, "POST": requests.post, "PUT": requests.put, "DELETE": requests.delete,
           "HEAD": requests.head,  "OPTIONS": requests.options, "PATCH": requests.patch}

for m in methods:
    for p in methods:
        response4 = methods[m]("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": p})
        if m != p and response4.text == '{"success":"!"}':
            print(response4.text)
            print(m, p)
        elif m == p and response4.text != '{"success":"!"}':
            print(response4.text)
            print(m, p)
