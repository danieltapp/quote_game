import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('http://quotes.toscrape.com')
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all(class_="quote")

with open('quotes.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['quote', 'author', 'url'])
    for quote in quotes:
        text = quote.find(class_='text').get_text()
        author = quote.find(class_='author').get_text()
        url = quote.find('a').attrs['href']
        csv_writer.writerow([text, author, url])


