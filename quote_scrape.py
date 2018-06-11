import requests
from bs4 import BeautifulSoup
from csv import DictWriter
from time import sleep



base_url = 'http://quotes.toscrape.com'

def scrape_quotes():
    all_quotes = []
    page = '/page/1'
    while page:
        response = requests.get(f'{base_url}{page}')
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                'text' : quote.find(class_='text').get_text(),
                'author' : quote.find(class_='author').get_text(),
                'url' : quote.find('a').attrs['href']
            })
        next = soup.find(class_="next")
        page = next.find("a")['href'] if next else None
        sleep(1)
    return all_quotes


quotes = scrape_quotes()

with open('quotes.csv', 'w') as file:
    headers = ['text', 'author', 'url']
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for quote in quotes:
        csv_writer.writerow(quote)










