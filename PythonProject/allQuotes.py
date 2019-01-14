from datetime import datetime
import requests
from bs4 import BeautifulSoup


def daily_quote():
    page = 5;

    while page < 7:
        url = 'https://www.goodreads.com/quotes/tag/wisdom?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.findAll('div', {'class': 'quoteText'}):
            quote = link.findAll(text=True, recursive=False)
            quote = quote[0]
            quote = quote[8:-5]
            print("\"" + quote + "\",")
        page += 1



daily_quote()

'''
   # entire_div = soup.findAll("div.quoteText")



    quote = entire_div.findAll(text=True, recursive=False)
    quote = quote[0]
    quote = quote[8:-5]

   # print(entire_div)

    fw = open('quote.txt', 'w')
    fw.truncate()
    fw.write(quote)
    fw.close
'''

