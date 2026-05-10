import pytest

@pytest.mark.parametrize('page', ['Alerts'], indirect=True)
def test_alert_page(page, alerts_page):
    alerts_page.open(page)
    alerts_page.click_button()
    assert alerts_page.alerts() == 'I am an alert!'