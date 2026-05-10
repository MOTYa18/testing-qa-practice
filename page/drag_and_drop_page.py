from page.base_page import BasePage
from page.locators import DragAndDrop

class DragAndDropPage(BasePage):
    def drag_and_drop(self):
        drag = self.element_is_visible(DragAndDrop.DRAG_ME)
        drop = self.element_is_visible(DragAndDrop.DROP_HERE)
        self.action().click_and_hold(drag).move_to_element(drop).release().perform()

    def get_drag_and_drop_text(self):
        return self.element_is_visible(DragAndDrop.RESULT).text