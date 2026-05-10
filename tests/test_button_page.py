import pytest

@pytest.mark.parametrize('page', ['Buttons'], indirect=True)
def test_click_button(page, button_page):
    button_page.open(page)
    button_page.click_button()

    assert button_page.check_result()

