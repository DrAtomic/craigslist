import pandas as pd
import json
from os.path import exists
import locate
import dataclean
import webscrape
import craigEmail

def create_listing(states,item):
    "takes list of states and item returns searched listing and creates \
    a csv of listings"
    statelinks = locate.stateLinks(states)
    searched = locate.searchLinks(statelinks,item)
    searched.to_csv('listings.csv',index=False,header=True)
    return searched

if __name__ == '__main__':
    
    #config
    with open("cfg.json") as file:
        config = json.load(file)
    states = config['states']
    item = config['item']
    lowerprice = config['lowerprice']
    upperprice = config['upperprice']
    
    #check for csv
    if exists("listings.csv"):
        print('listings csv exists do you want to use that?: ')
        answer = input()
        if answer == 'y':
            #use same listing
            searched = pd.read_csv('listings.csv')
        else:
            #create new listing
            searched = create_listing(states,item)
    else:
        #create new listing
        searched = create_listing(states, item)
        
    #dataclean
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
        crawling.to_csv('listings.csv',index=False,header=True)
        
        #email section
        # subject = item
        # body = "body of message here"
        # sender = "sender email address"
        # password = "password to sender email"
        
        # craigEmail.sendEmail(crawling, subject, body, sender, password)
