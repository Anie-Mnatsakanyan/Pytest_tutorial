from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from laptop_pages.base_page import BasePage
from locators.laptop_locators import full_login_url
from locators.login_locators import login_email, login_pass, login_button, LOGOUT_LINK


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email, timeout=5):
        self.enter_text(login_email, email,timeout)

    def enter_password(self,password, timeout=5):
        self.enter_text(login_pass, password,timeout)

    def click_login_button(self,timeout=5):
        self.click_element(login_button, timeout)

    def login(self,email,password):
        self.open_url(full_login_url)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button(timeout=5)

    def logout(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LOGOUT_LINK)).click()
            return True
        except Exception as e:
            print(f"Logout failed: {str(e)}")
            return False
