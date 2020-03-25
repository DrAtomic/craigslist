#!/usr/bin/env python3

from selenium import webdriver
import time
import pandas as pd


def crawl(df):
    "gets email information"
    email = []
    browser = webdriver.Firefox()
    for i in df.index:
        browser.get(df['link'][i])
        try:
            button = browser.find_element_by_css_selector('.reply-button')
            button.click()
            time.sleep(3)
            email.append(browser.find_element_by_css_selector('.mailapp').text)
        except:
            email.append("link not found")

    browser.quit()

    email_dataFrame = pd.DataFrame({'email':email})
    newDataframe = df.join(email_dataFrame)

    newDataframe.to_csv('dataWithEmail.csv',index=False,header=True)

    return newDataframe
