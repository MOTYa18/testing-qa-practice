from page.base_page import BasePage
from page.locators import *

class SelectPage(BasePage):
    def click_forms(self):
        self.element_is_clickable(SELECT.FORMS).click()
    
    def choise(self, i):
        self.element_is_clickable(SELECT.CHOISE(i)).click()

    def click_sumbit(self):
        self.element_is_clickable(SELECT.SUMBIT_BUTTON).click()

    def check(self):
        return self.element_is_visible(SELECT.RESULT).text