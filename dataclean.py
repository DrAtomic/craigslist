#!/usr/bin/env python3

import pandas as pd

def plot(fileName):
    import matplotlib.pyplot as plt
    import seaborn as sns
    df = pd.read_csv(fileName + '.csv')
    sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
    plt.show()

def priceData(fileName,lower,upper):
    "takes in file name and price range and returns clean data"
    df = pd.read_csv(fileName + '.csv')

    def impute_price(cols):
        "takes price columns colums and removes $"
        price = cols[0]
        if pd.isnull(price):
            return 0
        else:
            return int(price.replace("$",""))

    df['price'] = df[['price']].apply(impute_price,axis=1)

    #price range
    df= df[df['price'] != lower]
    df = df[df['price']< upper]
    
    df.to_csv('clean' + fileName + '.csv',index=False,header=True)
    return df

def name(data, *args):
    "takes a dataframe and a list of words that wont be displayed in the title"
    for i in args:
        data = data[~data.title.str.contains(i)]
    return data

if __name__ == "__main__":
    filename = 'file name'
    data = priceData(filename,0,100)
    df = name(data,"words","you","dont","want")

    df.to_csv('data.csv',index=False,header=True)
