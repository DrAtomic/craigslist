from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd


def crawl(df):
    "gets email information"
    email = []
    browser = webdriver.Firefox()
    for i in df.index:
        browser.get(df['link'][i])
        try:
            browser.find_element_by_css_selector('.reply-button').click()
            WebDriverWait(browser, timeout=1000, poll_frequency=1).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.show-email'))).click()
            time.sleep(2)
            email.append(browser.find_element_by_css_selector('.mailapp').text)
        except:
            email.append("link not found")

    browser.quit()

    email_dataFrame = pd.DataFrame({'email':email})
    newDataframe = df.join(email_dataFrame)

    return newDataframe
