import requests
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup


def save_html(html, path):
    with open(path, 'wb') as file:
        file.write(html)


def open_html(path):
    with open(path, 'wb') as file:
        return file.read()


URL = 'https://www.cardplayer.com/poker-players'
base = 'https://www.cardplayer.com/poker-players?page='
URLs = [base + str(i) + '&tab=all-players' for i in range(2, 20)]

cols = []

for link in URLs:
    response = requests.get(link)
    save_html(response.content, 'pokersite')

    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.select('tbody tr')

    name = rows[0].select_one('.player-player-name').text.strip()
    print(name)

    for row in rows:
        col = row.find_all('td')
        col = [x.text.strip() for x in col]
        cols.append(col)

    sleep(1)


index = ['Name', 'Country', 'Earnings', 'Cache']
df = pd.DataFrame(cols, columns=index)
print(df)
