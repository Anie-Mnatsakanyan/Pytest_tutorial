import time

from Tools.scripts.verify_ensurepip_wheels import print_notice
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.laptop_locators import currency, product_price, currency_code_, product_tools
from tests.conftest import driver

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def scroll_through_page(self, scroll_step=300, pause_time=0.5):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        for i in range(0, last_height, scroll_step):
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(pause_time)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        for i in range(last_height, 0, -scroll_step):
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(pause_time)

        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)



    def check_element_visibility(self, element):
        by, value = element
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))
            ActionChains(self.driver).move_to_element(element).perform()
            assert element.is_displayed(), f"Element {value} is not visible!"
            print(f"✅ Element {value} is visible.")
        except Exception as e:
            raise AssertionError(f"Element {value} not found: {str(e)}")

    def get_locator_type(self, locator):

        if locator.startswith('/'):
            return By.XPATH
        else:
            return By.ID

    def select_currency(self, currency_code):
        currency_dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(currency))
        currency_dropdown.click()
        print("currency_dropdown is clickable")
        currency_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(@href, '?set_currency={currency_code.lower()}')]")))
        currency_option.click()
        print("option is clickable")
        WebDriverWait(self.driver, 10).until(EC.url_contains(f"set_currency={currency_code.lower()}"))

        print(f"Currency selected: {currency_code.upper()}")


    def get_product_prices(self):
        #prices = self.driver.find_elements(product_price)
        prices = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(product_price))

        return [float(price.text.replace("$", "").replace(",", "")) for price in prices]

    def get_currency_code(self):
        currency_code_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(currency_code_))
        print(currency_code_element)
        #return currency_code_element.text.strip() # "USD" or "CAD"

    def enter_text(self,locator,text,timeout=5):
        element = WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def click_element(self,locator,timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def find_element(self, locator):
        #self.driver.find_element(*locator)
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(locator))

    def hover_and_verify_resize(self,image_locator, timeout=5):
        self.click_element(product_tools)

        image_element = self.find_element(image_locator)

        original_size = image_element.size
        original_width = original_size['width']
        original_height = original_size['height']

        action = ActionChains(self.driver)
        action.move_to_element(image_element).perform()
        time.sleep(3)

        print(original_size)
        new_size = image_element.size
        new_width = new_size['width']
        new_height = new_size['height']


        print(new_size)
        if new_width > original_width and new_height > original_height:
             print(
                 f"✅ Image resized successfully from {original_width}x{original_height} to {new_width}x{new_height}")
             return True
        else:
             print(f"❌ Image did not resize correctly ")

