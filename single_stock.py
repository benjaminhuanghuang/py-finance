
# -*- coding: utf-8 -*-
'''
    Download .csv fire from page http://quotes.money.163.com/
'''

from urllib import urlretrieve
f = open('sha.csv', 'r')
for lin in f   
    data = line.spilt()
    strock_no = '0' + data[0].replace('\"', "")
    start_data = data[1].replace('.',"").replace('\"', "")
    url = "http://quotes.money.163.com/service/chddata.html?code="+stock_no+"fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;MCAP"
    filename = stock_no+ '.csv'
    urlretrieve(url, filename)
