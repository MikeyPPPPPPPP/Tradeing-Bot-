import requests
from bs4 import BeautifulSoup
'''Thios modual will handle getting data like stock prices'''

def getStock(stock) -> str:
    '''This function will scrap google for the current price'''
    url = f'https://www.google.com/search?q={stock}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    for x in soup.findAll('span', {'jsname':'vWLAgc'}):
        return str(x.text)
    