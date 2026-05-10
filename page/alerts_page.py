from page.base_page import BasePage
from page.locators import *

class AlertsPage(BasePage):
    def click_button(self):
        self.element_is_clickable(ALERTS.MAIN_BUTTON).click()

    def alerts(self):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text