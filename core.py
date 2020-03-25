#!/usr/bin/env python3
import pandas as pd
import locate
import dataclean
import webscrape
import craigEmail

#locate
states = ['lowercase state abv']
item = "item you are searching for"
lowerprice = 0
upperprice = 500
statelinks = locate.stateLinks(states)
searched = locate.searchLinks(statelinks,item)

#dataclean
searched.to_csv('beforebreak.csv',index=False,header=True)
searched = pd.read_csv('beforebreak.csv')
priced = dataclean.priceData(searched,lowerprice,upperprice)
nameFix = dataclean.name(priced,item)
print(nameFix)
print('do you want to continue?: ')
x = input()
if x == 'n':
    exit()
else:
    #webscrape
    crawling = webscrape.crawl(nameFix)
    crawling.to_csv('dataEmail.csv')
    #email section

    subject = item
    body = "body of message here"
    sender = "sender email address"
    password = "password to sender email"

    craigEmail.sendEmail(crawling, subject, body, sender, password)
