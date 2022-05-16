import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

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
