# Description

This tool can be used to search through all the postings on craigslist
for a given state or list of states and return a csv, with  all the
post titles, price, link to listing.

# Requirements

```
pip install -R requirements.txt
```

## Optional
There is an optional plot of the dataframe for missing prices, i thought
it was useful so I left it in

```
pip install matplotlib
pip install seaborn
```

# Usage

Usage is not ideal right now, you have to manually go into core.py and edit the
states list, item, lowerprice, upperprice. for example

```
states = ['ca']
item = "toilet paper"
lowerprice = 10
upperprice = 500
```
after that is edited run 

```
python core.py
```

# Motivation

It was early in the pandemic and I decided to buy a graphics card, I was young and
carefree. I bought my graphics card online, when it finally arrived I picked up 
the box and thought "wow these things are getting light" I open the box and it was
empty. Someone at UPS opened the box and stole the graphics card. That changed me.
I thought to myself "what would I do if I were a lowly criminal that steals graphics
cards? I would sell it on craigslist" so I designed this program to find the perpetrator
and send him to the proper authorities to be hanged for crimes against humanity. I have 
yet to find the criminal, they are still out there. However my focus changed a few weeks
later. 

It was the great toilet paper run of 2020. Lunatics everywhere were buying and 
hoarding toilet paper. They truly believed that in a pandemic world there would be 
no toilet paper and that their bottoms would never be clean again.

A select few of the lunatics decided that toilet paper was the new cash crop and tried 
to sell toilet paper on craigslist, these wackos truly believed that someone would
pay 10$ per roll. Blinded by rage I finished this program.
I designed this program to look for an item and email the lister.
They needed to know that they were fools and I took it upon myself to let them know.

I have returned to this project because there are still lunatic scalpers out there.
