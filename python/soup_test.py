from bs4 import BeautifulSoup
import requests


def get_soup(url):
    html_soup = requests.get(url)
    soup = BeautifulSoup(html_soup.text, 'lxml')
    return soup.find_all(class_="message-userContent")


def get_plans(posts):
    for el in posts:
        el = str(el.text)
        return el.split("\n")


def plan_counts(arr, plan_count):

    for i in arr:
        if i.startswith("[X]") or i.startswith("[x]"):
            if i in plan_count:
                plan_count[i] += 1
            else:
                plan_count[i] = 1
    return plan_count


def send_plan(plans, url):
    for plan in plans:
        data ={"plan":next(iter(plan)), "votes":plan.next(iter(plan))}
        requests.post(url, data)