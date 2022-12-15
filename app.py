import time

import requests
from bs4 import BeautifulSoup

user_name = "maiermarc75"


def get_users(tab):
    page = 0
    users = []
    while True:
        page += 1
        url = f"https://github.com/{user_name}?page={page}&tab={tab}"
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, features="html.parser")
        follow_list = soup.find_all("turbo-frame")[0].find_all(
            "div", attrs={"class": "d-table"}
        )
        if not follow_list:
            break
        users += [
            x.find_all("div", attrs={"class": "d-table-cell"})[1].a["href"][1:]
            for x in follow_list
        ]
        time.sleep(3)
    return users


followings = get_users("following")
followers = get_users("followers")
long = followings if len(followings) >= len(followers) else followers
short = followings if len(followings) < len(followers) else followers
print(long)
print(short)
print([x for x in long if x not in short])
