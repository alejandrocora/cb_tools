import re
from selenium.webdriver.common.by import By

def getNewAssetDate(driver):
    elems = driver.find_elements(By.XPATH, '//p[@class="cds-typographyResets-t1xhpuq2 cds-body-bvviwwo cds-foregroundMuted-f1vw1sy6 cds-transition-txjiwsi cds-start-s1muvu8a"]')
    elem = elems[1]
    return elem.text.split(' ')[-2:]

def getNewAssetName(driver):
    elems = driver.find_elements(By.XPATH, '//p[@class="cds-typographyResets-t1xhpuq2 cds-headline-hb7l4gg cds-foreground-f1yzxzgu cds-transition-txjiwsi cds-start-s1muvu8a"]')
    elem = elems[1]
    return elem.text
