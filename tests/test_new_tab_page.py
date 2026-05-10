import pytest
from page.locators import URL

@pytest.mark.parametrize('page', ['Link'], indirect=True)
def test_new_tab_page(page, new_tab_page):
    new_tab_page.open(page)
    new_tab_page.click_button()
    new_tab_page.switch_tab()
    new_tab_page.original_element_new_page()
    assert new_tab_page.get_url() == URL.NEW_LINK