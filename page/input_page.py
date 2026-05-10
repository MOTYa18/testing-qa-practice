from page.locators import INPUT
from page.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class InputPage(BasePage):

    def click_string_field(self):
        self.element_is_visible(INPUT.STRING_FIELD).click()

    def write(self, text):
        self.element_is_visible(INPUT.STRING_FIELD).send_keys(text)

    def tab_enter(self):
        self.element_is_visible(INPUT.STRING_FIELD).send_keys(Keys.ENTER)

    def get_result_text(self):
        return self.element_is_visible(INPUT.RESULT_TEXT).text
    
    def error_visible(self):
        return self.element_is_visible(INPUT.ERROR).is_displayed()