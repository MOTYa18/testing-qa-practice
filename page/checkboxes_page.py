from page.locators import CHECKBOXES
from page.base_page import BasePage

class CheckboxesPage(BasePage):
    def click_select(self):
        self.element_is_clickable(CHECKBOXES.SELECT_BUTTON).click()

    def click_sumbit(self):
        self.element_is_clickable(CHECKBOXES.SUMBIT_BUTTON).click()

    def check_result(self):
        return self.element_is_visible(CHECKBOXES.RESULT)

