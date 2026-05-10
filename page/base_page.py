import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def action(self):
        return ActionChains(self.driver)

    def open(self, page):
        return page

    def element_is_visible(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def element_is_clickable(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def get_url(self):
        return self.driver.current_url
    
    def switch_new_tab(self, i):
        self.driver.switch_to.window(self.driver.window_handles[i])