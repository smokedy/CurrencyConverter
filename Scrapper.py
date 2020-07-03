from bs4 import BeautifulSoup
import requests

def Currencyscrapper(quantidade,moedainicial,moedafinal,var_resultado):
    page = requests.get('http://conversordemoedas.co/{}-{}-{}'.format(quantidade,moedainicial,moedafinal))
    html_code = BeautifulSoup(page.content, 'html.parser')
    amount = (html_code.find('strong', class_='resultamount').get_text())
    var_resultado.set(amount)



