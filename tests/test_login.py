from selenium.webdriver.support.wait import WebDriverWait
import pytest
from laptop_pages.login_page import LoginPage
from locators.login_locators import error_message
from test_data.login_data import invalid_email, invalid_pass, valid_email, valid_pass

@pytest.mark.test2
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(invalid_email, invalid_pass)
    error = login_page.find_element(error_message).text
    assert "Error! Wrong e-mail or password."in error