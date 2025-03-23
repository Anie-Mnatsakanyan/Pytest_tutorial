import pytest
from selenium.webdriver.common.by import By

base_url = "https://www.laptopscreen.com/English/"
login_url = "section/account_login/"
full_login_url = base_url + login_url

header = (By.XPATH, '//*[@id="ver-1"]')
footer = (By.XPATH, "/html/body/footer")
middle = (By.XPATH, "/html/body/main/div")
product_link = (By.CSS_SELECTOR, "body > main > div > div > div > div > p > a:nth-child(1)")
currency = (By.XPATH,'//*[@id="top"]/div/div/div[4]')#dropdown
product_price = (By.XPATH, "/html/body/main/div/div[5]/div[4]/div[2]/b")
currency_code_ = (By.CSS_SELECTOR, '#top > div > div > div.col.dsk-span-1.tbt-span-1.drop-down.js-drop-down.currency-dropdown > div.label.text-upc > span.dsk-only.currency_text' )
product_tools = (By.XPATH, '//*[@id="ver-1"]/div[3]/div/div[4]/div/a[2]')
image_locator = (By.XPATH, '/html/body/main/div/div[2]/div[1]')

