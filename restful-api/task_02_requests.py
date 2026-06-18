#!/usr/bin/python3
import requests


def fetch_and_print_posts():
    try:
        r = requests.get("https://jsonplaceholder.typicode.com/posts")
        print("Status Code: ", r.status_code)
        if (r.status_code == 200):
            responses = r.json()
            for response in responses:
                print(response)
        pass
    except Exception as e:
        raise e
