import requests
import json

def get_quotes(keyword):
    """ Get a list of quotes from quote garden api in json format."""
    url = f'https://quote-garden.herokuapp.com/api/v3/quotes?query={keyword}&page=1&limit=10'
    response = requests.get(url)
    return json.loads(response.content)

def clean_data(quotes_data):
    """ Take the quote and author, format it and put it in a list. """
    quotes_list = quotes_data['data']
    formatted_quotes = []
    for quote in quotes_list:
        quote_formatted = f"{quote['quoteText']} - {quote['quoteAuthor']}"
        formatted_quotes.append(quote_formatted)

    return formatted_quotes
  
def main():
    """ Takes user input and prints the list of pre-formatted quotes. """
    keyword = input('Enter a keyword: ')
    quotes_data = get_quotes(keyword)
    quotes_formatted = clean_data(quotes_data)
    for quote in quotes_formatted:
        print(quote)

if __name__ == '__main__':
    main()