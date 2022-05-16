import re
from selenium.webdriver.common.by import By

def getAssetAMT(driver):
    elem = driver.find_element(By.XPATH, '//span[@class="Text__Font-sc-163p65w-0 jaOSJx PaginationBar__Results-sc-1dqgh2r-4 jldbVe"]')
    return int(re.findall("\w+", elem.text)[-2])
