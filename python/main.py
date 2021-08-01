from selenium import webdriver
import requests
from bs4 import BeautifulSoup
chrome_driver_path = r"C:\Users\Hazel\OneDrive\Desktop\mfd discord\python\chromedriver_win32 (2)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


indexing = True
chapter_url_mfd = ""

MFD_Role = 824002066439602196

plan_link_mfd = []


def get_soup(plan_count):
    html_soup = requests.get((driver.current_url))
    soup = BeautifulSoup(html_soup.text, 'lxml')
    li = soup.find_all(class_="message-userContent")
    for el in li:
        el = str(el.text)
        arr = el.split("\n")
        for i in arr:
            if i.startswith("[X]") or i.startswith("[x]"):
                if i in plan_count:
                    plan_count[i] += 1
                else:
                    plan_count[i] = 1



def get_mfd():
    global chrome_driver_path
    global driver
    chrome_driver_path = r"C:\Users\Hazel\OneDrive\Desktop\mfd discord\python\chromedriver_win32 (2)\chromedriver.exe"

    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.minimize_window()

    driver.get(
        "https://forums.sufficientvelocity.com/threads/marked-for-death-a-rational-naruto-quest.24481/")
    print(driver.current_url)
    current_chapter = driver.find_elements_by_partial_link_text("Chapter")
    print(current_chapter)
    current_chapter[-1].click()


def get_links():
    global link_to_mfd
    s = 1
    link = driver.find_elements_by_css_selector(".message-attribution-main  a")
    print(link)
    for item in link:
        nl = item.get_attribute("href")
        if "member" not in nl and "page" not in nl and "reader" not in nl:
            link_to_mfd.append(nl)
    return link_to_mfd


def get_plan():
    global vote_count_mfd
    s = 1
    post = driver.find_elements_by_class_name("bbWrapper")
    for i in post:
        print(f"{i.text}\n{s}\n\n\n\n\n")
        s += 1
    print(len(post))
    for i in range(len(post)):
        if "[X]" in post[i].text or "[x]" in post[i].text:

            with open(f"vote{vote_count_mfd}.txt", "w",  encoding="utf-8") as data:
                data.write(f"{post[i].text}\n{link_to_mfd[i + 3]}")
                vote_count_mfd += 1


def forward_page():
    global PAGE_COUNT
    next_page = driver.find_element_by_partial_link_text("Next")
    page_link = next_page.get_attribute("href")
    page_num = (page_link.partition("page-")[::-1])
    driver.get(
        f"https://forums.sufficientvelocity.com/threads/marked-for-death-a-rational-naruto-quest.24481/page-{page_num[0]}")



def get_plans_and_links():
    get_mfd()
    while indexing == True:
        try:
            forward_page()
        except:
            driver.quit()
            indexing == False
            break


get_plans_and_links()
print("eeeyyyy")