#!/usr/bin/env python3

# New Asset WArning (nawa)

import os
import argparse
from time import sleep

from lib.getListed import *
from lib.waitLoad import *
from lib.getNewAsset import *
from lib.checkTelegram import *
from lib.selaux import *

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
