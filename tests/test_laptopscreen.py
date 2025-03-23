import time

import pytest

from laptop_pages.base_page import BasePage
from laptop_pages.login_page import LoginPage
from locators import laptop_locators
from locators.laptop_locators import base_url, image_locator


def test_base_page_ui(driver):
    base_page = BasePage(driver)
    base_page.open_url(base_url)
    base_page.scroll_through_page()
    base_page.check_element_visibility(laptop_locators.header)
    base_page.check_element_visibility(laptop_locators.footer)
    base_page.check_element_visibility(laptop_locators.middle)

@pytest.mark.parametrize("currency_code", ['CAD','USD'])
def test_currency_conversion(driver, currency_code):
    base_page = BasePage(driver)
    base_page.open_url(base_url)
    base_page.select_currency(currency_code)

    selected_currency = base_page.get_currency_code()


    print(currency_code)
    print(selected_currency)
    assert currency_code == selected_currency, f"Currency mismatch! Expected {currency_code}, but found {selected_currency}"

@pytest.mark.test1
def test_hover(driver):
    base_page = BasePage(driver)
    base_page.open_url(base_url)

    result = base_page.hover_and_verify_resize(image_locator)
    assert result, "Test failed: Image did not resize correctly."