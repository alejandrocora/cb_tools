#!/usr/bin/env python3

# New Asset WArning (nawa)

import os
import argparse
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait

from cb_lib.get_new_asset import *
from cb_lib.check_tel_config import *
from cb_lib.selaux import *

def get_change(LAF, browtype):
    change = None
    try:
        f = open(LAF, 'x')
        f.close()
    except:
        pass
    f = open(LAF, 'r+')
    lastAsset = f.read().split('\n')
    if not browtype:
        driver = headless_firefox()
    else:
        driver = headless_chrome()
    driver.get('https://www.coinbase.com/price/s/listed')
    WebDriverWait(self.driver, 120).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="LoadingBlock__Overlay-f50e0a-2 kgHxKT"]'))
    )
    newAssetDate = ' '.join(get_new_asset_date(driver))
    newAssetName = get_new_asset_name(driver)
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
    parser.add_argument('--firefox', dest='browtype', default=False, action='store_false')
    parser.add_argument('--chrome', dest='browtype', action='store_true')
    args = parser.parse_args()
    delay = args.delay
    LAF = args.file
    browtype = args.browtype
    telconfig = check_tel_config()
    if not telconfig:
        print('[!] There is no telegram-send configuration!')
    while telconfig:
        change = get_change(LAF, browtype)
        if change:
            os.system('telegram-send --format html "❕ A 🆕 Asset has been added ➡️ <b>' + change[0] + '</b> (' + change[1] + ')"')
        sleep(delay)

if __name__ == '__main__':
    main()
