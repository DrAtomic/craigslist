#!/usr/bin/env python3

import pandas as pd

def plot(df):
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
    plt.show()

def priceData(df,lower,upper):
    "takes in file name and price range and returns clean data"

    def impute_price(cols):
        "takes price columns colums and removes $"
        price = cols[0]
        if pd.isna(price):
            return 0
        else:
            return int(price.replace("$",""))

    df['price'] = df[['price']].apply(impute_price,axis=1)
    #price range
    df= df[df['price'] != lower]
    df = df[df['price']< upper]

    #df.to_csv('cleanData.csv',index=False,header=True)
    return df

def name(data, *args):
    "takes a dataframe and a list of words that must be displayed in the title"
    for i in args:
        data = data[data.title.str.contains(i)]
    return data


if __name__ == "__main__":
    df = pd.read_csv("name of csv")
    data = priceData(df,0,100)
    print(data)
    df = name(data,"words","you","want")
    df.to_csv('final.csv',index=False,header=True)
