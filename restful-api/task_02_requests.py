#!/usr/bin/env python3
import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get("title"))

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    if r.status_code == 200:
        posts = r.json()

    data_toSave = [
            {
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
            }
            for post in posts
            ]

    with open("posts.csv", mode='w', encoding='utf-8', newline='') as f:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_toSave)

    else:
        pass
