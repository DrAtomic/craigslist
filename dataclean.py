#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def clean(fileName):
    df = pd.read_csv(fileName + '.csv')
    #sns.heatmap(df.isnull(),yticklabels = False,cbar=False,cmap='viridis')
    def impute_price(cols):
        price = cols[0]
        if pd.isnull(price):
            return 0
        else:
            return int(price.replace("$",""))
    df['price'] = df[['price']].apply(impute_price,axis=1)

    df.to_csv('clean' + fileName + '.csv',index=False,header=True)
    sns.heatmap(df.isnull(),yticklabels = False,cbar=False,cmap='viridis')
    plt.show()

filename = 'toilet paper'
clean(filename)
