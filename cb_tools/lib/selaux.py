import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_Options
from selenium.webdriver.firefox.options import Options as firefox_Options

def headless_chrome():
    options = chrome_Options()
    options.add_argument('--headless')
    options.add_argument("user-agent=Chrome/99.0.4844.51")
    driver  = webdriver.Chrome(options=options)
    return driver

def headless_firefox():
        options = firefox_Options()
        options.add_argument('--headless')
        options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0")
        driver  = webdriver.Firefox(firefox_options=options, service_log_path=os.devnull)
        return driver
