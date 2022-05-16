#!/usr/bin/env python3

# New Asset WArning (nawa)

import os
import argparse
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

from lib.getListed import *
from lib.waitLoad import *
from lib.getNewAsset import *
from lib.checkTelegram import *

def headlessChrome():
    options = Options()
    options.add_argument('--headless')
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")
    driver  = webdriver.Chrome(options=options)
    return driver

def headlessFirefox():
        options = Options()
        options.add_argument('--headless')
        driver  = webdriver.Firefox(options=options, service_log_path=os.devnull)
        return driver

def getChange(LAF):
    change = None
    try:
        f = open(LAF, 'x')
        f.close()
    except:
        pass
    f = open(LAF, 'r+')
    lastAsset = f.read().split('\n')
    driver = headlessFirefox()
    getListed(driver)
    waitLoad(driver)
    newAssetDate = ' '.join(getNewAssetDate(driver))
    newAssetName = getNewAssetName(driver)
    if ((lastAsset[0] != newAssetName) or (lastAsset[1] != newAssetDate)):
        f.close()
        f = open(LAF, 'w')
        f.write(newAssetName+'\n'+newAssetDate)
        change = [newAssetName, newAssetDate]
    f.close()
    driver.close()
    return change

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--delay', type=int, default=600, help='Delay time in seconds.')
    parser.add_argument('-f', '--file', type=str, default='lastAsset.txt', help='Filename to store the last Asset information.')
    args = parser.parse_args()
    delay = args.delay
    LAF = args.file
    telconfig = checkTelegram()
    if not telconfig:
        print('[!] There is no telegram-send configuration!')
    while telconfig:
        change = getChange(LAF)
        if change:
            os.system('telegram-send --format html "❕ A 🆕 Asset has been added ➡️ <b>' + change[0] + '</b> (' + change[1] + ')"')
        sleep(delay)

if __name__ == '__main__':
    main()
