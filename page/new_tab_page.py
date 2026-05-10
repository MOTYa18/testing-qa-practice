from page.base_page import BasePage
from page.locators import *

class NewTabPage(BasePage):

    def click_button(self):
        self.element_is_visible(NewTab.LINK_BUTTON).click()

    def switch_tab(self):
        return self.switch_new_tab(1)

    def original_element_new_page(self):
        return self.element_is_visible(NewTab.RESULT_TEXT)
    


