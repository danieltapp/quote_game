import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

base_url = 'http://quotes.toscrape.com'

def read_quotes(filename):
    with open(filename, 'r') as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

quotes = read_quotes('quotes.csv')


def game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote : ")
    print(quote['text'])
    guess = ''
    while guess.lower() != quote['author'].lower() and remaining_guesses > 0:
        guess = input(f'Who said this? Guesses remaining : {remaining_guesses}. \n').lower()
        if guess == quote['author'].lower():
            print('you win!!!')
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{base_url}{quote['url']}")
            soup = BeautifulSoup(res.text, 'html.parser')
            born_date = soup.find(class_="author-born-date").get_text()
            born_location = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint : The author was born on {born_date} {born_location}")
        elif remaining_guesses == 2:
            print(f"The author's first name start's with {quote['author'][0]}")
        elif remaining_guesses == 1:
            print(f"The author's last name start's with {quote['author'].split(' ')[1][0]}")
        else:
            print(f"Sorry, you ran out of guesses. The answer is : {quote['author']}")
    again = ''
    while again not in ('y', 'yes', 'n', 'no'):
        again = input("Play again? (y / n)")
    if again.lower() in ('y', 'yes'):
        return game(quotes)
    else:
        print('Goodbye')

game(quotes)









