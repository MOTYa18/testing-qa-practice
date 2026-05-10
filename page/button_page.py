from page.base_page import BasePage
from page.locators import BUTTON

class ButtonPage(BasePage):

    def click_button(self):
        return self.element_is_clickable(BUTTON.BUTTON_CLICK).click()
    
    def check_result(self):
        return self.element_is_visible(BUTTON.RESULT)
    
    
