from selenium.webdriver.common.by import By
class URL:
        INPUT = 'https://www.qa-practice.com/elements/input/simple'
        BUTTONS = 'https://www.qa-practice.com/elements/button/simple'
        CHECKBOXES = 'https://www.qa-practice.com/elements/checkbox/single_checkbox'
        SELECT = 'https://www.qa-practice.com/elements/select/single_select'
        LINK = 'https://www.qa-practice.com/elements/new_tab/link'
        TEXTAREA = 'https://www.qa-practice.com/elements/button/simple'
        ALERTS = 'https://www.qa-practice.com/elements/alert/alert'
        DRAGNDROP = 'https://www.qa-practice.com/elements/dragndrop/boxes'
        POPUP = 'https://www.qa-practice.com/elements/popup/modal'
        IFRAMES = 'https://www.qa-practice.com/elements/iframe/iframe_page'
        NEW_LINK = 'https://www.qa-practice.com/elements/new_tab/new_page'

class INPUT:
        STRING_FIELD = (By.ID, 'id_text_string')
        RESULT_TEXT = (By.ID, 'result-text')
        ERROR = (By.ID, 'error_1_id_text_string')

class BUTTON:
        BUTTON_CLICK = (By.ID, 'submit-id-submit')
        RESULT = (By.ID, 'result')

class CHECKBOXES:
        SELECT_BUTTON = (By.ID, 'id_checkbox_0')
        SUMBIT_BUTTON = (By.ID, 'submit-id-submit')
        RESULT = (By.ID, 'result')

class SELECT:
        FORMS = (By.ID, 'id_choose_language')
        SUMBIT_BUTTON = (By.ID, 'submit-id-submit')
        RESULT = (By.ID, 'result-text')
        
        @staticmethod
        def CHOISE(i):
                return (By.XPATH, f'//*[@id="id_choose_language"]/option[{i}]')
        
class NewTab:
        LINK_BUTTON = (By.ID, 'new-page-link')
        RESULT_TEXT = (By.ID, 'result')
class ALERTS:
        MAIN_BUTTON = (By.CSS_SELECTOR, 'a.a-button')

class DragAndDrop:
       DRAG_ME = (By.ID, 'rect-draggable')
       DROP_HERE = (By.ID, 'rect-droppable')
       RESULT = (By.ID, 'text-droppable')