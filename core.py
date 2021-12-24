import pandas as pd
import json
import locate
import dataclean
import webscrape
import craigEmail

if __name__ == '__main__':
    
    #config
    with open("cfg.json") as file:
        config = json.load(file)
    states = config['states']
    item = config['item']
    lowerprice = config['lowerprice']
    upperprice = config['upperprice']
    #locate
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
        # subject = item
        # body = "body of message here"
        # sender = "sender email address"
        # password = "password to sender email"
        
        # craigEmail.sendEmail(crawling, subject, body, sender, password)
