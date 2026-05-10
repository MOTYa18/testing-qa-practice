import pytest

@pytest.mark.parametrize('page', ['Drag-n-drop'], indirect=True)
def test_drag_n_drop(page, drag_and_drop_page):
    drag_and_drop_page.open(page)
    drag_and_drop_page.drag_and_drop()
    assert drag_and_drop_page.get_drag_and_drop_text() == 'Dropped!'