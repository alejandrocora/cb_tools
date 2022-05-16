import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

def headless_chrome():
    options = Options()
    options.add_argument('--headless')
    driver  = webdriver.Chrome(options=options)
    return driver

def headless_firefox():
        options = Options()
        options.add_argument('--headless')
        driver  = webdriver.Firefox(options=options, service_log_path=os.devnull)
        return driver
