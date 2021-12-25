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
    states = config['search']['states']
    item = config['search']['item']
    lowerprice = config['search']['lowerprice']
    upperprice = config['search']['upperprice']
    
    #check for csv
    if exists("listings.csv"):
        answer = input('listings csv exists do you want to use that?[y/n]: ')
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
    answer = input('do you want to continue?[y/n]: ')
    if answer == 'n':
        exit()
    else:
        #webscrape
        crawling = webscrape.crawl(nameFix)
        crawling.to_csv('listings.csv',index=False,header=True)
        
        #email section
        subject = config['email']['subject']
        body = config['email']['body']
        sender = config['email']['address']
        password = config['email']['password']
            
        craigEmail.sendEmail(crawling, subject, body, sender, password)
