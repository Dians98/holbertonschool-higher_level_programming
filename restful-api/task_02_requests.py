#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    try:
        r = requests.get("https://jsonplaceholder.typicode.com/posts")
        print("Status Code: ", r.status_code)
        if (r.status_code == 200):
            responses = r.json()
            for response in responses:
                print(response)
        else:
            print(f"Failed to fetch data. Status Code: {r.status_code}")
    except Exception as e:
        raise e


def fetch_and_save_posts():
    try:
        r = requests.get("https://jsonplaceholder.typicode.com/posts")
        print("Status Code: ", r.status_code)
        if (r.status_code == 200):
            posts = r.json()

            data = [
                {'id': post['id'],
                 'title': post['title'],
                 'body': post['body']}
                for post in posts
            ]

            with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=['id', 'title', 'body'])

                writer.writeheader()

                writer.writerows(data)
        else:
            print(f"Failed to fetch data. Status Code: {r.status_code}")
        pass
    except Exception as e:
        raise e
