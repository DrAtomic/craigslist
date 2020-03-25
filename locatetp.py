#!/usr/bin/env python3

import bs4
from requests import get
import pandas as pd

def stateLinks(states):
    "takes a list of states and produces a list of sublinks"
    res = []
    soup = []
    links = []
    for i in range(len(states)):
        res.append(get('https://geo.craigslist.org/iso/us/'+states[i]))
        soup.append(bs4.BeautifulSoup(res[i].text))

    #adds data for each soup
    for j in range(len(soup)):
        data = soup[j].findAll('ul',attrs={'class':'geo-site-list'})
        rawlinks = data[0].findAll('a',href=True)

        for k in range(len(rawlinks)):
            links.append(rawlinks[k]['href'])
    return links

def searchLinks(links,search):
    "takes list of links and search item returns a dataframe of list"
    searchAd = []
    linkAd = []
    priceAd = []
    for link in links:
        response = get(link + '/search/sss?query='+ search +'&sort=rel')
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        posts = soup.find_all('li', class_= 'result-row')
        post_title_texts = []
        post_links = []
        post_prices = []
        for post in posts:
            if post.find('span', class_ = 'result-hood') is not None:
                post_title = post.find('a', class_='result-title hdrlnk')
                post_title_text = post_title.text
                post_title_texts.append(post_title_text.lower())
                post_link = post_title['href']
                post_links.append(post_link)
                post_price = post.a.text.strip()
                post_prices.append(post_price)

        for i in range(len(post_title_texts)):
            if (post_title_texts[i].find(search) != -1):
                searchAd.append(post_title_texts[i])
                linkAd.append(post_links[i])
                priceAd.append(post_prices[i])

    searchAdDf = pd.DataFrame({'title':searchAd,
                               'link':linkAd,
                               'price':priceAd})

    searchAdDf.to_csv(search+'.csv',index=False,header=True)
    return searchAdDf

states = ['ca']
links = stateLinks(states)
data = searchLinks(links,"search item")
print(data)
print('done')
