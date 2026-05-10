import pytest
from selenium import webdriver
from page.locators import URL
from page.input_page import InputPage
from page.button_page import ButtonPage
from page.checkboxes_page import CheckboxesPage
from page.select_page import SelectPage
from page.new_tab_page import NewTabPage
from page.alerts_page import AlertsPage
from page.drag_and_drop_page import DragAndDropPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture
def page(request, driver):
    param = request.param
    if param == 'Input':
        driver.get(URL.INPUT)
    elif param == 'Buttons':
        driver.get(URL.BUTTONS)
    elif param == 'Checkboxes':
        driver.get(URL.CHECKBOXES)
    elif param == 'Select':
        driver.get(URL.SELECT)
    elif param == 'Link':
        driver.get(URL.LINK)
    elif param == 'TextArea':
        driver.get(URL.TEXTAREA)
    elif param == 'Alerts':
        driver.get(URL.ALERTS)
    elif param == 'Drag-n-drop':
        driver.get(URL.DRAGNDROP)
    elif param == 'Pop-Up':
        driver.get(URL.POPUP)
    elif param == 'Iframes':
        driver.get(URL.IFRAMES)
    
@pytest.fixture
def input_page(driver):
    return InputPage(driver)

@pytest.fixture
def button_page(driver):
    return ButtonPage(driver)

@pytest.fixture
def checkboxes_page(driver):
    return CheckboxesPage(driver)

@pytest.fixture
def select_page(driver):
    return SelectPage(driver)

@pytest.fixture
def new_tab_page(driver):
    return NewTabPage(driver)

@pytest.fixture
def alerts_page(driver):
    return AlertsPage(driver)

@pytest.fixture
def drag_and_drop_page(driver):
    return DragAndDropPage(driver)