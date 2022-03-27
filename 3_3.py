'''
#1
import requests
from bs4 import BeautifulSoup

a, b = (input() for _ in range(2))

def link_search(link_a):
    soup = BeautifulSoup(requests.get(link_a).content, "html.parser")
    links = set()
    for link in soup.find_all('a'):
        if link == "" or link is None:
            # href пустой тег
            continue
        links.add(link.attrs.get("href"))
    return links

indicator = False
for c in link_search(a):
    c_links = link_search(c)
    if b in c_links:
        print('Yes')
        indicator = True
        break

if indicator is False:
    print('No')
'''

#2

import requests, re

from bs4 import BeautifulSoup

firth_link = str(input())
soup = BeautifulSoup(requests.get(firth_link).content, "html.parser")

pattern_link = r'''(?:href=)(?:['"])(?:\w*://)?(\w[\w\.\-]+)(?:[/:'"])'''

links = set()
for link in soup.find_all('a'):
    link = str(link)
    link = re.findall(pattern_link, link)
    for l in link:
        if l == '':
            continue
        links.add(l)
links = sorted(links)
print('\n'.join(links))

'''
<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">
'''