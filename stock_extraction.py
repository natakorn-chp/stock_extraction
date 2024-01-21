import requests
import re
import json
from bs4 import BeautifulSoup
from datetime import datetime

def main(url):

    rsp = requests.get(url)  # get data from a given url

    if rsp.status_code in (200,):   # check status code is 200 or not 
        s = BeautifulSoup(rsp.text, 'lxml')
        symbol = s.find_all('h2', {'class':'GLlpnb'})         # get a symbol of desied stock
        price = s.find_all('div', {'class':'YMlKec fxKbKc'})  # get a desied stock's price

        symbol_lst = rmOthstr(str(symbol[0])).split(' • ')    # tranform symbol data
        symbol = symbol_lst[0]                                
        price = rmOthstr(str(price[0]))                       # tranform stock's price
        dateNow = str(datetime.today())                       # get datetime now

    data = {'symbol':symbol, 'price':price, 'uint':'baht', 'datetime':dateNow} # encapsulate data as dict
    print('the result is',data)
    saveData(data)

def rmOthstr(txt):
    reg_bkt = '\<.*?\>'
    tmp_txt = re.sub(reg_bkt,'',txt)
    
    reg_bth = '฿'
    tmp_txt = re.sub(reg_bth,'',tmp_txt)
    
    return tmp_txt

def saveData(data):
    app_json = json.dumps(data) # encapsulate data as json form

    with open('{enter_your_path}/stkToday.txt', 'w') as outfile: # save the data as text file for saving into database
        json.dump(data, outfile)



url = 'https://www.google.com/finance/quote/SET50:INDEXBKK?output=json'
main(url)





