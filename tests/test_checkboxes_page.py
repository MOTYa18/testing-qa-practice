import pytest

@pytest.mark.parametrize('page', ['Checkboxes'], indirect=True)

def test_sumbit_button(page, checkboxes_page):
    checkboxes_page.open(page)
    checkboxes_page.click_select()
    checkboxes_page.click_sumbit()
    assert checkboxes_page.check_result