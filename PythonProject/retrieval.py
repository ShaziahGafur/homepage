from datetime import datetime
import requests
from bs4 import BeautifulSoup

day_year = datetime.now().timetuple().tm_yday


def daily_quote(day_year):
    page = day_year // 30 + 1
    item_number = day_year - (page - 1) * 30
    url = 'https://www.goodreads.com/quotes/tag/wisdom?page=' + str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    entire_div = soup.select("div.quoteText")[item_number - 1]
    quote = entire_div.findAll(text=True, recursive=False)
    quote = quote[0]
    quote = quote[8:-5]
    '''
    #first_pos = quote_temp.find('\n') + 8
    #if first_pos == 7:
    #first_pos = quote_temp.find("\n") + 8
    #quote = quote[first_pos:]
    #last_pos = quote.find('\n')
    #quote = quote[:last_pos]
    '''
    print(quote)


daily_quote(day_year)