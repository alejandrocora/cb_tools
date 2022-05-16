from selenium.webdriver.common.by import By
from time import sleep

def wait_load(driver):
    found = True
    max = 99
    count = 0
    while found and count < max:
        try:
            elem = driver.find_element(By.XPATH, '//div[@class="LoadingBlock__Overlay-f50e0a-2 kgHxKT"]')
            count += 1
            sleep(1)
        except:
            found = False
