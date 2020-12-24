import csv
import json
import requests as re

USER_ID: int
HOST_ID: str
URL = 'https://api.webmaster.yandex.net/v4/user/{user_id}/hosts/{host_id}/recrawl/queue'
URL.format(user_id=USER_ID, host_id=HOST_ID)


def request(url, link_sending_list):
    response_list = {}
    for link_sending in link_sending_list:
        data = {
            "url": "{}".format(link_sending)
        }
        response = re.post(url=url, data=data)
        response_list[link_sending] = response
    return response_list



with open('../file_output/result.json', "r") as file:
    data = json.load(file)

    for elem in data:
        print("old"+elem)
        print("new"+ data[elem][0])