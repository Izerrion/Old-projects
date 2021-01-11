# To run ctrl+shift+b

import requests
from bs4 import BeautifulSoup

jobs = []
descr = []
type = []
urls = []

base_url = 'https://freelance.ru'
prefix_url = 'https://freelance.ru/projects/?spec=116'
for j in range (10):
    URL = prefix_url+'&page='+str(j+1)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(class_='ptitle')
    if len(results) == 0:
        print('We are done')
        break
    results2 = soup.find_all(class_='descr')
    results3 = soup.find_all('li', class_='status')
    results4 = []

    for item in results2:
        results4.append(item['href'])


    for item in results:
        jobs.append(item.find('span').text)

    for item in results2:
        descr.append(item.find_all('span')[1].text)


    for item in results3:
        type.append(item.text)

    for item in results4:
        urls.append(base_url + item)


print(len(jobs))
print(jobs)
print(descr)
print(type)
print(urls)

with open('index.html', 'w') as file:
    for job,des,typ,url in zip(jobs, descr, type, urls):
        template = '<h1>' + job + '</h1>' + '<h2>' + typ + '</h2>' + '<p>' + des + '</p><br><a>' + url + '</a><br><br>'
        file.write(template)
