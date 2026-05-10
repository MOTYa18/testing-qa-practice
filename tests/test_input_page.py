import pytest

@pytest.mark.parametrize('page', ['Input'], indirect=True)

def test_valid_data(page, input_page):
    input_page.open(page)
    input_page.click_string_field()
    input_page.write("hello")
    input_page.tab_enter()

    assert input_page.get_result_text() == 'hello'

@pytest.mark.parametrize('page', ['Input'], indirect=True)
def test_no_valid(page, input_page):
    input_page.open(page)
    input_page.click_string_field()
    input_page.write("h")
    input_page.tab_enter()
    assert input_page.error_visible()